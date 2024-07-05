#!/usr/bin/python3
"""
This script sends a request to a URL and
displays the body of the response.
"""


import sys
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode())

    except HTTPError as e:
        print("Error code: ", e.code)
