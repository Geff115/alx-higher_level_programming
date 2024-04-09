#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Rectangle class with width and height.
        """

        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Getting width.
        """

        return self._width

    @width.setter
    def width(self, value):
        """
        Set width.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getting height.
        """

        return self._height

    @height.setter
    def height(self, value):
        """
        setting height.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
