#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for i, char in enumerate(str):
        if i == n:
            continue
        else:
            result += char
    return result
