#!/usr/bin/python3
"""This is a square class that inherits
from a rectangle class.
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
    """This is a child class"""

    def __init__(self, width, height):
        """Initialization method for the child lass
        with height and width as private attributes.
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This is an area method that returns width * height"""

        return (self.__height * self.__width)

    def __str__(self):
        """String representation method"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """This class inherits from Rectangle class"""

    def __init__(self, size):
        """Initialization method for the subclass to validate size"""

        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area method"""

        return (self.__size ** 2)
