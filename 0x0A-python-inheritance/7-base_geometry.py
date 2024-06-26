#!/usr/bin/python3
"""A Base Geometry class"""


class BaseGeometry:
    """This is a class"""

    def area(self):
        """This is a method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This is a method"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
