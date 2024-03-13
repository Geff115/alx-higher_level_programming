#!/usr/bin/python3
def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return "Enter only two integers to add"
