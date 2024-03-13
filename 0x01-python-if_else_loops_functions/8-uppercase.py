#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = ord(i) - 32
            result += chr(i)
        elif i.isalpha():
            result += i
        else:
            result += i
    print("{}".format(result))
