#!/usr/bin/python3
"""Text indentation module."""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        while i < len(text) and text[i] == ' ':
            i += 1

        line = ""
        while i < len(text):
            line += text[i]
            if text[i] in '.?:':
                print(line.rstrip())
                print()
                i += 1
                break
            i += 1
        else:
            if line.strip():
                print(line.rstrip())
