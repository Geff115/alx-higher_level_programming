#!/usr/bin/python3
"""This class has a prive instance
attribute and init method.
"""


import json


class Base:
    """This is a class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a Python object to JSON string"""

        if not list_dictionaries:
            return ("[]")

        else:
            return (json.dumps(list_dictionaries))
