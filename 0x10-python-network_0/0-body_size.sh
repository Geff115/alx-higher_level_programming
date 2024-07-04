#!/bin/bash
# This script takes a URL and sends a request to that URL
curl -s -I $1 | grep 'Content-Length' | awk '{print $2}'
