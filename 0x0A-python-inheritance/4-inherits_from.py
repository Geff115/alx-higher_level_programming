#!/usr/bin/python3
"""This function returns true if an object is an
instance of a class it inherits from directly or indirectly.
"""


def inherits_from(obj, a_class):
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
