#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable.
"""


import sys
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
