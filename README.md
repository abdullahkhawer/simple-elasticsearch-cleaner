# Simple Elasticsearch Cleaner

- Founder: Abdullah Khawer (LinkedIn: https://www.linkedin.com/in/abdullah-khawer/)

# Introduction

A simple Elasticsearch cleaner based on a Python script to clean up all indices and data streams
from the Elasticsearch cluster which are older than the specified number of days.

Below you can find an example of the execution:
```
simple-elasticsearch-cleaner % python simple_elasticsearch_cleaner.py 30
Script Execution Started!
Calculating the date that was 30 day(s) ago...
Connecting to Elasticsearch...
Connected to Elasticsearch successfully.
Fetching the list of all the data streams...
Fetching the list of all the indices...
Finding and deleting all the indices older than 30 days '2024.07.14'...
Deleted index '__REDACTED__' which was created on '2024.07.12'.
Deleted index '__REDACTED__' which was created on '2024.07.13'.
Deleted index '__REDACTED__' which was created on '2024.07.12'.
Deleted index '__REDACTED__' which was created on '2024.07.13'.
Finding and deleting all the data streams older than 30 days '2024.07.14'...
Skipping data stream '__REDACTED__' as it is a managed data stream.
Skipping data stream '__REDACTED__' as it is a managed data stream.
Deleted data stream '__REDACTED__' which was older than '2024.07.14'.
Deleted data stream '__REDACTED__' which was older than '2024.07.14'.
Skipping data stream '__REDACTED__' as it is a managed data stream.
Closing the connection with Elasticsearch...
Connection with Elasticsearch closed successfully.
Script Execution Completed!
```

Note: In the actual execution, you will see the actual values instead of `__REDACTED__` values.

# Usage Notes

## Prerequisites

Following are the prerequisites to be met once before you begin:

- Following packages should be installed on your system:
   - `pip`
   - `python`
   - `elasticsearch`
      - Using `pip`

## Execution Instructions

Once all the prerequisites are met, set the following environment variables:
   - `ELASTICSEARCH_HOST`
      - Description: Host of Elasticsearch cluster.
      - Example: `https://localhost`
      - Requirement: REQUIRED
   - `ELASTICSEARCH_PORT`
      - Description: Port of Elasticsearch cluster.
      - Example: `9200`
      - Requirement: REQUIRED
   - `ELASTICSEARCH_USER`
      - Description: Username of the Elasticsearch cluster.
      - Example: `admin`
      - Requirement: REQUIRED
   - `ELASTICSEARCH_PASSWORD`
      - Description: Password of the user of the Elasticsearch cluster.
      - Example: `123456789`
      - Requirement: REQUIRED

And then simply run the following command:
- `python simple_elasticsearch_cleaner.py NUMBER_OF_DAYS`
   - Example: `python simple_elasticsearch_cleaner.py 30`

#### Any contributions, improvements and suggestions will be highly appreciated. 😊
