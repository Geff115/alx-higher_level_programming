#!/usr/bin/python3
"""A Square class that inherits from
a Rectangle class.
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """A Square is a special rectangle, so it
    inherits all the attributes of the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method for the square class,
        and  it calls the init of the parent.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation method using the getters
        in the Rectangle class.
        """

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Getter method for the size"""

        return (self.width)

    @size.setter
    def size(self, value):
        """Setter method for the size"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must be > 0")

        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """Handling variable number of arguments and also
        keyword arguments.
        """

        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """A method that returns a dictionary representation."""

        return ({
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        })
