#!/bin/bash
# This script makes a request to a URL, and the server respond with a message.
curl -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" -sL 0.0.0.0:5000/catch_me
