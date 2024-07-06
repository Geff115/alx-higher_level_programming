#!/usr/bin/python3
"""
This script prints the HTTP status code.
If the HTTP status code is greater than or equal to 400,
it prints Error code followed by the value of the HTTP
status code.
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    status = response.status_code
    if status >= 400:
        print("Error code:", status)
    else:
        print(response.text)
