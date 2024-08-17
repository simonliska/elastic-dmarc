#!/bin/bash
unzip -n /var/cache/raw/\*.zip -d /var/cache/dmarc-reports
cd /var/cache/raw/
gunzip -k *.gz
mv *.xml /var/cache/dmarc-reports/