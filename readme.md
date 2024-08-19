# elastic dmarc ingestor

## Description

This project is a simple script that fetches dmarc reports from a mail server, unzips them and sends them to an elastic search instance.

## Installation

crontab:

```bash
0 * * * * python3 /var/cache/scripts/fetch.py && . /var/cache/scripts/unzip.sh
```

### Datadog config example

Untested, but should work.

`./datadog/conf.yaml` 
