#!/usr/bin/python3

from calculation_1 import add, sub

def magic_calculation(a, b):
    if a < b:
        c = a + b
        for i in range(4, 6):
            c = add(c, i)
        return c

    else:
        return sub(a, b)
