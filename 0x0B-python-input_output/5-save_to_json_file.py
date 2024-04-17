#!/usr/bin/python3
"""Importing JSON module"""


import json


def save_to_json_file(my_obj, filename):
    """This function writes into a file using json representation
    string.

    ARGS:
        my_obj: The object in form of json string to be written
                into the file.
        filename: The file to store the object.
    """

    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
