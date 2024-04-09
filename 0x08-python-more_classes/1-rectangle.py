#!/usr/bin/python3
"""A Rectangle class with width and
height properties.
"""


class Rectangle:
    """This is a class"""

    def __init__(self, width=0, height=0):
        """Initialization method"""

        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter method"""

        return (self._width)

    @width.setter
    def width(self, value):
        """Setter method"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter method"""

        return (self._height)

    @height.setter
    def height(self, value):
        """Setter method"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
