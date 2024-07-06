#!/usr/bin/python3
"""
This script takes in a URL and an email address,
sends a POST request to the passed URL with the email
as a parameter, and finally displays the body of the
reponse.
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email_address = sys.argv[2]
    data = {'email': email_address}
    response = requests.post(url, data=data)
    print(response.text)
