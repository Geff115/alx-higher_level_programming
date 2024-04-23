#!/usr/bin/python3
"""This class has a prive instance
attribute and init method.
"""


import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        into a file.
        """

        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        if os.path.exists(cls.__name__ + '.json'):
            with open(cls.__name__ + '.json', mode='r') as file:
                data = file.read()
                return (json.loads(data))
        else:
            with open(cls.__name__ + '.json', mode='w') as file:
                file.write(json_str)
