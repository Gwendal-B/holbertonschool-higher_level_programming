#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
