#!/usr/bin/python3
"""This is a Python script"""


class Student:
    """This is a student class with public instance
    attributes with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """Initialization method of the public instances"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A method that returns a dictionary representation of
        a Student object.
        """

        return (vars(self))
