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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
