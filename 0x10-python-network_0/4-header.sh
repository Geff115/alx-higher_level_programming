#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"
