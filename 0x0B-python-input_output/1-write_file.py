#!/usr/bin/python3
"""This is a Python script that runs a python
task.
"""


def write_file(filename="", text=""):
    """This function writes a string to a text file"""

    with open(filename, mode='w', encoding='UTF-8') as file:
        file.write(text)
    return (len(text))
