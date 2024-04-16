#!/usr/bin/python3
"""This is a Python script that runs Python
tasks.
"""


def append_write(filename="", text=""):
    """This function appends a text at the end of
    a file.
    """

    with open(filename, mode='a', encoding='UTF-8') as file:
        file.write(text)
    return (len(text))
