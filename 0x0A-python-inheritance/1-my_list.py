#!/usr/bin/python3
"""This class is a subclass that inherits
from a parent class.
"""


class MyList(list):
    """This is a class"""

    def print_sorted(self):
        """This is a method of the class"""

        sorted_list = sorted(self)
        sorted_string = '[' + ', '.join(str(e) for e in sorted_list) + ']'
        print(sorted_string)
