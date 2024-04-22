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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for the width"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method for the width"""

        self.__width = value

    @property
    def height(self):
        """Getter method for the height"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for the height"""

        self.__height = value

    @property
    def x(self):
        """Getter method for x"""

        return (self.__x)

    @x.setter
    def x(self, value):
        """Setter method for x"""

        self.__x = value

    @property
    def y(self):
        """Getter method for y"""

        return (self.__y)

    @y.setter
    def y(self, value):
        """Setter method for y"""

        self.__y = value
