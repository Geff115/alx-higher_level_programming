#!/usr/bin/python3
"""This function opens a file and closes it
automatically using the with statement.
"""


def read_file(filename=""):
    """This function opens a file called filename
    which is an empty string.
    """

    with open(filename, encoding='UTF-8') as file:
        print(file.read(), end="")
