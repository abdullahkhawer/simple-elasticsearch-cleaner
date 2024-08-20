# Quick Reference

-	**Maintained by**:
	[Abdullah Khawer - LinkedIn](https://www.linkedin.com/in/abdullah-khawer)

-	**Maintained at**:
	[simple-elasticsearch-cleaner - GitHub](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner)

-	**Where to file issues**:
	[https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/issues](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/issues)

# Supported tags and respective `Dockerfile` links

-	[`2.0.0`, `latest`](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/v2.0.0/docker/Dockerfile)

# Simple Elasticsearch Cleaner

- Founder: [Abdullah Khawer - LinkedIn](https://www.linkedin.com/in/abdullah-khawer)

# Introduction

A simple Elasticsearch cleaner based on a Python script to delete all indices and data streams from the Elasticsearch cluster which are older than the specified number of days. It is basically a curator but with the ability to delete only, removing both indices and their associated data streams.

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

*Note: In the actual execution, you will see the actual values instead of `__REDACTED__` values.*

For more details, check out its repository on GitHub [here](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/).

# Usage Notes

## Execution Instructions

Set the following environment variables:
   - `ELASTICSEARCH_HOST`
      - Description: Host of Elasticsearch cluster.
      - Example: `https://localhost`
      - Requirement: REQUIRED
   - `ELASTICSEARCH_PORT`
      - Description: Port of Elasticsearch cluster.
      - Example: `9200`
      - Requirement: REQUIRED
   - `ELASTICSEARCH_USER`
      - Description: Username of the user of the Elasticsearch cluster.
      - Example: `admin`
      - Requirement: REQUIRED
   - `ELASTICSEARCH_PASSWORD`
      - Description: Password of the user of the Elasticsearch cluster.
      - Example: `123456789`
      - Requirement: REQUIRED
   - `NUMBER_OF_DAYS`
      - Description: Number of days to delete the indices and data streams older than that.
      - Example: `30`
      - Requirement: REQUIRED

And then simply run the following command:
- `docker run --platform linux/amd64 -it -e ELASTICSEARCH_HOST=$ELASTICSEARCH_HOST -e ELASTICSEARCH_PORT=$ELASTICSEARCH_PORT -e ELASTICSEARCH_USER=$ELASTICSEARCH_USER -e ELASTICSEARCH_PASSWORD=$ELASTICSEARCH_PASSWORD -e NUMBER_OF_DAYS=$NUMBER_OF_DAYS abdullahkhawer/simple-elasticsearch-cleaner:latest`

## Build Command

Following build command is used on the root level in the GitHub repository:

`docker buildx build --platform linux/amd64 -t "abdullahkhawer/simple-elasticsearch-cleaner:latest" --no-cache -f ./docker/Dockerfile .`

# License

This project is licensed under the Apache License - see the [LICENSE](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/LICENSE) file for details.

#### Any contributions, improvements and suggestions will be highly appreciated. 😊
