#!/usr/bin/python3
"""This is a Python script."""


class Student:
    """This is a student class with public instance
    attributes with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """Initialization method of the public attributes."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A method that retrieves a dictionary representation
        of a student class.
        """

        new_dict = {}
        if isinstance(attrs, list) and all(isinstance(elem, str)
                                           for elem in attrs):
            for i in attrs:
                if hasattr(self, i):
                    value = getattr(self, i)
                    new_dict[i] = value
            return (new_dict)
        else:
            return (vars(self))
