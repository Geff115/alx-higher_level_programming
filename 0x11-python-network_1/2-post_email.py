#!/usr/bin/python3
"""
This script sends a POST request to a passed URL
with the email as a parameter and displays the
body of the response.
"""


import sys
from urllib.request import urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    data = urlencode({'email': sys.argv[2]}).encode()
    with urlopen(sys.argv[1], data) as response:
        print(response.read().decode())
