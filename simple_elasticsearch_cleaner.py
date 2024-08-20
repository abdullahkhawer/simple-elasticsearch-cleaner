#!/usr/bin/python

"""
A simple Elasticsearch cleaner based on a Python script to clean up all indices and data streams
from the Elasticsearch cluster which are older than the specified number of days.
"""

# required imports
import os
import sys
from datetime import datetime, timedelta, timezone
import urllib3
from elasticsearch import Elasticsearch

print("Script Execution Started!")

# fetch environment variables related to Elasticsearch
elasticsearch_host = os.getenv("ELASTICSEARCH_HOST")
elasticsearch_port = os.getenv("ELASTICSEARCH_PORT")
elasticsearch_user = os.getenv("ELASTICSEARCH_USER")
elasticsearch_password = os.getenv("ELASTICSEARCH_PASSWORD")
number_of_days = os.getenv("NUMBER_OF_DAYS")
if elasticsearch_host is None:
    print("ERROR: ELASTICSEARCH_HOST environment variable is not set.")
    sys.exit(1)
if elasticsearch_port is None:
    print("ERROR: ELASTICSEARCH_PORT environment variable is not set.")
    sys.exit(1)
if elasticsearch_user is None:
    print("ERROR: ELASTICSEARCH_USER environment variable is not set.")
    sys.exit(1)
if elasticsearch_password is None:
    print("ERROR: ELASTICSEARCH_PASSWORD environment variable is not set.")
    sys.exit(1)
if number_of_days is None:
    print("ERROR: NUMBER_OF_DAYS environment variable is not set.")
    sys.exit(1)

# calculate the date that was {number_of_days} days ago
print(f"Calculating the date that was {number_of_days} day(s) ago...")
older_date = (datetime.now() - timedelta(days=int(number_of_days))).strftime('%Y.%m.%d')

# mute warnings for Elasticsearch client as certificate verification is disabled
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# connect to Elasticsearch
print("Connecting to Elasticsearch...")
elasticsearch_client = Elasticsearch(
    [f"{elasticsearch_host}:{elasticsearch_port}"],
    basic_auth=(
        elasticsearch_user,
        elasticsearch_password
    ),
    verify_certs=False,
    ssl_show_warn=False
)

# verify the connection with Elasticsearch
elasticsearch_client.info()
print("Connected to Elasticsearch successfully.")

# fetch the list of all the data streams
print("Fetching the list of all the data streams...")
all_data_streams = elasticsearch_client.indices.get_data_stream(name="*")

# fetch the list of all the indices
print("Fetching the list of all the indices...")
all_indices = elasticsearch_client.indices.get(index="*")

# find and delete all the indices older than {number_of_days} days '{older_date}'
print(
    f"Finding and deleting all the indices older than {number_of_days} days '{older_date}'..."
)
data_stream_indices = []
for index in all_indices:
    # fetch the creation date of the index
    index_settings = elasticsearch_client.indices.get_settings(index=index)
    creation_date_in_ms = index_settings[index]['settings']['index']['creation_date']

    # format the creation date of the index
    creation_date_in_seconds = int(creation_date_in_ms) / 1000
    creation_datetime = datetime.fromtimestamp(creation_date_in_seconds, timezone.utc)
    formatted_creation_date = creation_datetime.strftime('%Y.%m.%d')

    # check if the creation date of the index is older than {number_of_days} days
    if older_date > formatted_creation_date:
        # check if the index is related to a data stream
        if ".ds" in index:
            # add the index in the list of data stream indices to delete its related data stream
            data_stream_indices.append(index)
        else:
            # delete the index
            elasticsearch_client.indices.delete(index=index)
            print(
                f"Deleted index '{index}' which was created on '{formatted_creation_date}'."
            )

# find and delete all the data streams older than {number_of_days} days '{older_date}'
print(
    f"Finding and deleting all the data streams older than {number_of_days} days '{older_date}'..."
)
for data_stream in all_data_streams['data_streams']:
    # fetch the name, management status, hidden status, system status and indices of the data stream
    data_stream_name = data_stream['name']

    # check if the data stream is a system, hidden and/or managed data stream
    if data_stream['system'] is True:
        print(f"Skipping data stream '{data_stream_name}' as it is a system data stream.")
    elif data_stream['hidden'] is True:
        print(f"Skipping data stream '{data_stream_name}' as it is a hidden data stream.")
    elif "_meta" in data_stream and data_stream['_meta']['managed'] is True:
        print(f"Skipping data stream '{data_stream_name}' as it is a managed data stream.")
    else:
        # check if any of indices of a data stream is older than {number_of_days} days
        for data_stream_index in data_stream['indices']:
            if data_stream_index['index_name'] in data_stream_indices:
                # delete the data stream
                elasticsearch_client.indices.delete_data_stream(name=data_stream_name)
                print(
                    f"Deleted data stream '{data_stream_name}' which was older than '{older_date}'."
                )
                break

# close the connection with Elasticsearch
print("Closing the connection with Elasticsearch...")
elasticsearch_client.transport.close()
print("Connection with Elasticsearch closed successfully.")

print("Script Execution Completed!")
