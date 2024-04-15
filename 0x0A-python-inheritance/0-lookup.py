#!/usr/bin/python3
"""This function returns a list of available
attributes and methods of an object.
"""


def lookup(obj):
    """This is a function"""

    obj_result = dir(obj)
    return (obj_result)
