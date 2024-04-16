#!/usr/bin/python3
"""A Rectangle class that inherits from
a parent class BaseGeometry.
"""


class BaseGeometry:
    """A BaseGeometry class"""

    def area(self):
        """Area method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates name to be a positive integer
        otherwise raise an error.
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """This is a class"""

    def __init__(self, width, height):
        """Initialization method"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
