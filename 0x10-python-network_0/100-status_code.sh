#!/bin/bash
# This script uses curl command with -s to fetchg the response of a certain URL
curl -s -o /dev/null -w "%{http_code}" $1
