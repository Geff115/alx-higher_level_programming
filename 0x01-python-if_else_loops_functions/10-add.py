#!/usr/bin/python3
def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, int) and isinstance(b, str):
        return "Error"
    else:
        return "Enter only two integers to add"
