#!/usr/bin/python3
"""A Rectangle class that inherits
from Base class.
"""


from .base import Base


class Rectangle(Base):
    """Rectangle class inheriting from
    Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method"""

        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        elif width <= 0:
            raise ValueError("width must be > 0")

        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        elif height <= 0:
            raise ValueError("value must be > 0")

        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        elif x < 0:
            raise ValueError("x must be >= 0")

        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        elif y < 0:
            raise ValueError("y must be >= 0")

        else:
            self.__y = y

    @property
    def width(self):
        """Getter method for the width"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method for the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must be > 0")

        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value <= 0:
            raise ValueError("value must be > 0")

        else:
            self.__height = value

    @property
    def x(self):
        """Getter method for x"""

        return (self.__x)

    @x.setter
    def x(self, value):
        """Setter method for x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        elif value < 0:
            raise ValueError("x must be >= 0")

        else:
            self.__x = value

    @property
    def y(self):
        """Getter method for y"""

        return (self.__y)

    @y.setter
    def y(self, value):
        """Setter method for y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        elif value < 0:
            raise ValueError("y must be >= 0")

        else:
            self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""

        return (self.__width * self.__height)

    def display(self):
        """Display method that prints the rectangle instance #"""

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """String representation method"""

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """This method handles variable number of arguments"""

        attributes = ['id', '__width', '__height', '__x', '__y']
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)

        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
