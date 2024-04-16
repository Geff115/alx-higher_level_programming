#!/usr/bin/python3
"""A rectangle class that inherits from a
BaseGeometry class.
"""


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
