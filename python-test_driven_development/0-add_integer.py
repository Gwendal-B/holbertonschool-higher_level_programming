#!/usr/bin/python3
"""Module that defines add_integer function."""


def add_integer(a, b=98):
    """Return the addition of two integers.

    a and b must be integers or floats.
    Floats are cast to integers before addition.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return a + b
