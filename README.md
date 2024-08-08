# Simple Elasticsearch Cleaner

- Founder: Abdullah Khawer (LinkedIn: https://www.linkedin.com/in/abdullah-khawer/)

# Introduction

A simple Elasticsearch cleaner based on a Python script to clean up all indices and data streams
from the Elasticsearch cluster which are older than the specified number of days.

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
