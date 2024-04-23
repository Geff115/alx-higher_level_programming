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
