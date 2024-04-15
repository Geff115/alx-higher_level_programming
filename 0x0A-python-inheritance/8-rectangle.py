#!/usr/bin/python3
"""A Rectangle class that inherits from
a parent class BaseGeometry.
"""


import importlib

BaseGeometry = importlib.import_module("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class"""

    def __init__(self, width, height):
        """Initialization method"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
