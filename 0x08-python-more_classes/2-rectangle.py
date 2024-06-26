#!/usr/bin/python3
"""A Rectangle class with perimeter
and area.
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
            raise ValueError("value must be >= 0")
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
            raise ValueError("value must be >= 0")
        self._height = value

    def area(self):
        """Area method"""

        return (self._width * self._height)

    def perimeter(self):
        """Perimeter method"""

        if self._width == 0 or self._height == 0:
            return (0)
        else:
            return (2 * (self._width + self._height))
