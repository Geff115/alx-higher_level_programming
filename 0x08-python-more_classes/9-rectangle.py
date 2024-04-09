#!/usr/bin/python3
"""A Rectangle class with
more and more functionalities
"""


class Rectangle:
    """This is a class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialization method"""

        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Area method"""

        return (self._width * self._height)

    def perimeter(self):
        """Perimeter method"""

        if self._width == 0 or self._height == 0:
            return (0)
        else:
            return (2 * (self._width + self._height))

    def __str__(self):
        """Str method"""

        if self._width == 0 or self._height == 0:
            return ("")
        row = str(self.print_symbol) * self._width
        return ("\n".join([row] * self._height))

    def __repr__(self):
        """Repr method"""

        return (f"Rectangle({self._width}, {self._height})")

    def __del__(self):
        """Del method"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
