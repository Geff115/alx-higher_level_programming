#!/bin/bash
# This script displays all HTTP methods a server will accept
curl -sI "$1" | grep "Allow"
