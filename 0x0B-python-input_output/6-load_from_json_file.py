#!/usr/bin/python3
"""Importing JSON module"""


import json


def load_from_json_file(filename):
    """This function returns an object from
    a JSON representation string.
    """

    with open(filename, mode='r') as f:
        return (json.load(f))
