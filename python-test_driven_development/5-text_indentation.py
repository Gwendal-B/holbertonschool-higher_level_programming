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

    break_chars = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in break_chars:
            line = text[start:i+1].strip()
            print(line)
            print()
            start = i + 1

    remaining = text[start:].strip()
    if remaining:
        print(remaining)
