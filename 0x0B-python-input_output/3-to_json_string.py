#!/usr/bin/python3
"""Using JSON to return a representation
of an object string.
"""


import json


def to_json_string(my_obj):
    """This function returns a json representation
    of an object string.
    """

    return (json.dumps(my_obj))
