#!/usr/bin/python3
"""Module that provides a function to read and print a text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF-8) and returns the
    number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
