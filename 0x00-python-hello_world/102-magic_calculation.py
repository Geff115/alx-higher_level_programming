#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98
    result += a * b
    return result

import dis
dis.dis(magic_calculation)
