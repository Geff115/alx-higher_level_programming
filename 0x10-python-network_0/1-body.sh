#!/bin/bash
# This script sends a GET request to a URL
curl -s -L -I "$1" | grep HTTP/ | awk '{print $2}' && curl -s -L "$1"
