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

# Usage Notes

Following are the 4 ways to use it:
- Python script.
- Docker container running that Python script.
- Helm chart to create a Helm release to create a cron job running that Docker container in a pod on a Kubernetes cluster.
- Terraform module to deploy that Helm chart as a Helm release on a Kubernetes cluster.

## Terraform Module

You can use its [Terraform module](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/terraform) to create a Helm release using its Helm chart to create a cron job running that Docker container in a pod on a Kubernetes cluster.

For more details, check out its [README](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/terraform/README.md).

## Helm Chart

You can use its [Helm chart](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/helm-charts/simple-elasticsearch-cleaner) to create a Helm release to create a cron job running that Docker container in a pod on a Kubernetes cluster.

For more details, check out its [README](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/helm-charts/simple-elasticsearch-cleaner/README.md).

## Docker Image

You can use its [Docker image](https://hub.docker.com/r/abdullahkhawer/simple-elasticsearch-cleaner/) which is publicly available to run its Docker container to run its Python script.

The Dockerfile used to build the image can be found [here](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/docker).

For more details, check out its [README](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/docker/README.md).

## Python Script

You can use its [Python script](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/simple_elasticsearch_cleaner.py) to run it directly which is the main script to be executed in order to clean the old indices and data streams.

### Prerequisites

Following are the prerequisites to be met once before you begin:

- Following packages should be installed on your system:
   - `pip`
   - `python`
   - Using `pip`, install the following via `requirements.txt` file:
      - `urllib3`
      - `elasticsearch`

### Execution Instructions

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
- `python simple_elasticsearch_cleaner.py`

# License

This project is licensed under the Apache License - see the [LICENSE](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/LICENSE) file for details. This LICENSE file applies to all the code in this repository including `docker`, `helm-charts` and `terraform` subdirectories.

#### Any contributions, improvements and suggestions will be highly appreciated. 😊
