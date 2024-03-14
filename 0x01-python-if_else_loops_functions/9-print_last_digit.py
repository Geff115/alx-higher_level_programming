#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    return f"{last_digit}"


print(print_last_digit(98))
print(print_last_digit(0))
r = print_last_digit(-1024)
print(r)
