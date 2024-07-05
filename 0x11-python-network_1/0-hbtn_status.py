#!/usr/bin/python3
"""
This script fetches a certain URL using urllib
"""


from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        for lines in response:
            decoded_lines = lines.decode()
            splitted_lines = decoded_lines.split("\n")
            for line in splitted_lines:
                print("Body response:")
                print("\t- type:", type(lines))
                print("\t- content:", lines)
                print("\t- utf8 content:", decoded_lines)
