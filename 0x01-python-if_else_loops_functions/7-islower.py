#!/usr/bin/python3
def islower(c):
    if c.isdigit():
        return False
    elif ord(c) >= 32 and ord(c) <= 47:
        return False
    elif ord(c) >= 58 and ord(c) <= 64:
        return False
    elif ord(c) >= 91 and ord(c) <= 96:
        return False
    elif ord(c) >= 123 and ord(c) <= 126:
        return False
    else:
        return 97 <= ord(c) <= 122


print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
