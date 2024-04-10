#!/usr/bin/python3
"""A class with no object or
class attribute.
"""


class LockedClass:
    """This is a class"""

    def __setattr__(self, name, value):
        """Setattr method"""

        if name != 'first_name' or hasattr(self, name):
            raise AttributeError("Object has no attribute")
        super().__setattr__(name, value)
