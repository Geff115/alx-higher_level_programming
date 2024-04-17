#!/usr/bin/python3
"""Importing JSON module"""


import json


def from_json_string(my_str):
    """Returns an object represented by a
    json string.
    """

    return (json.loads(my_str))
