#!/usr/bin/python3
"""This is a Python script"""


def class_to_json(obj):
    """This function returns the dictionary decription
    for JSON serialization of an object.
    """

    return (obj.__dict__)
