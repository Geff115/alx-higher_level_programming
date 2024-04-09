#!/usr/bin/python3
"""More functionality in the
Rectangle class.
"""


class Rectangle:
    """This is a class"""

    number_of_instances = 0

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

    def area(self):
        """Area method"""

        return (self._width * self._height)

    def perimeter(self):
        """Perimeter attribute"""

        if self._width == 0 or self._height == 0:
            return (0)
        else:
            return (2 * (self._width + self._height))

    def __str__(self):
        """String representation method"""

        if self._width == 0 or self._height == 0:
            return ("")
        else:
            return ('\n'.join(['#' * self._width for _ in range(self._height)])
                    )

    def __repr__(self):
        """Repr method"""

        return (f"Rectangle({self._width}, {self._height})")

    def __del__(self):
        """Del method"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
