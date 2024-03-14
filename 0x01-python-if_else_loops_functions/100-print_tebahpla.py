#!/usr/bin/python3
def alternating_alphabet():
    for i in range(122, 65, -1):
        if i % 2 == 0 and i in range(97, 123):
            print("{}".format(chr(i)), end="")
        elif i % 2 != 0 and (i - 32) in range(65, 91):
            print("{}".format(chr(i - 32)), end="")


alternating_alphabet()
