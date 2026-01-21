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
        while i < len(text) and text[i] not in '.?:':
            line += text[i]
            i += 1

        if line.strip():
            print(line.rstrip(), end='')

        if i < len(text) and text[i] in '.?:':
            print(text[i])
            print()
            i += 1
