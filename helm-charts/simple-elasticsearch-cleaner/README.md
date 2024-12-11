# Simple Elasticsearch Cleaner

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

This Helm chart is a way to configure and run [Simple Elasticsearch Cleaner Docker image](https://hub.docker.com/r/abdullahkhawer/simple-elasticsearch-cleaner/) as a Docker container via a cron job in a pod on a Kubernetes cluster. It will create a Helm release to create that cron job.

## Setup

The default configuration file for this chart is configured in a way that you don't need to change anything but some configurations can be changed as desired.

The Helm chart uses Kubernetes secrets having Elasticsearch credentials which are host, username and password. You can either create new secret(s) or use existing one(s). You can specify the secret name and key for all 3 credentials via the values file as follows:

```yaml
secrets:
  host:
    name: "simple-elasticsearch-cleaner-secret"
    key: "elasticsearch-host"
  user:
    name: "elasticsearch-credentials"
    key: "elasticsearch-username"
  password:
    name: "elasticsearch-credentials"
    key: "elasticsearch-password"
```

Following are the details about the values of all 3 credentials in their Kubernetes secrets:
   - `elasticsearch-host`
      - Description: Host of Elasticsearch cluster.
      - Example: `https://localhost`
      - Requirement: REQUIRED
   - `elasticsearch-username`
      - Description: Username of the user of the Elasticsearch cluster.
      - Example: `admin`
      - Requirement: REQUIRED
   - `elasticsearch-password`
      - Description: Password of the user of the Elasticsearch cluster.
      - Example: `123456789`
      - Requirement: REQUIRED

## Installation, Upgrade and Uninstallation

* Clone the git repo: `git clone git@github.com:abdullahkhawer/simple-elasticsearch-cleaner.git`

* Installation: `helm install --namespace elasticsearch simple-elasticsearch-cleaner ./helm-charts/simple-elasticsearch-cleaner`

* Upgrade: `helm upgrade --namespace elasticsearch simple-elasticsearch-cleaner ./helm-charts/simple-elasticsearch-cleaner`

* Uninstallation: `helm uninstall --namespace elasticsearch simple-elasticsearch-cleaner`

*Note: You can choose your desired namespace instead of `elasticsearch`.*

## Configuration

| Parameter                      | Description                                                                                                                                                                  | Default                              |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| `image.tag`             | Image tag                                                                                      | `2.1.0`                 |
| `image.pullPolicy`        | Image pull policy                                                                                      | `Always`                                 |
| `namespace`        | Kubernetes namespace                                                                                      | `elasticsearch`                                 |
| `schedule`        | Cron job schedule                                                                                      | `0 1 * * *`                                 |
| `numberOfDays`        | To delete the indices and data streams older than the specified number of days                                                                                      | `30`                                 |
| `resources.limits.cpu`        | Pod CPU limit                                                                                      | `200m`                                 |
| `resources.limits.memory`        | Pod memory limit                                                                                      | `256Mi`                                 |
| `resources.requests.cpu`        | Pod CPU request                                                                                      | `100m`                                 |
| `resources.requests.memory`        | Pod memory request                                                                                      | `128Mi`                                 |
| `nodeSelector`        | Node selector for pod                                                                                      | `{}`                                 |
| `esPort`        | Elasticsearch port                                                                                      | `9200`                                 |
| `secrets.host.name`        | Name of Kubernetes secret having Elasticsearch host                                                                                      | `simple-elasticsearch-cleaner-secret`                                 |
| `secrets.host.key`        | Name of key inside Kubernetes secret having Elasticsearch host                                                                                      | `elasticsearch-host`                                 |
| `secrets.user.name`        | Name of Kubernetes secret having Elasticsearch username                                                                                      | `elasticsearch-credentials`                                 |
| `secrets.user.key`        | Name of key inside Kubernetes secret having Elasticsearch username                                                                                      | `elasticsearch-username`                                 |
| `secrets.password.name`        | Name of Kubernetes secret having Elasticsearch password                                                                                      | `elasticsearch-credentials`                                 |
| `secrets.password.key`        | Name of key inside Kubernetes secret having Elasticsearch password                                                                                      | `elasticsearch-username`                                 |

# License

This project is licensed under the Apache License - see the [LICENSE](https://github.com/abdullahkhawer/simple-elasticsearch-cleaner/blob/master/LICENSE) file for details.

#### Any contributions, improvements and suggestions will be highly appreciated. 😊
