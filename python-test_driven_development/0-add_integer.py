#!/usr/bin/python3
"""
Module that defines a function to add two integers.
Raises TypeError if inputs are not integers or floats.
"""
def add_integer(a, b=98):
    """Adds two integers and returns the result as an integer.
        a (int, float): The first integer.
        b (int, float): The second integer (default is 98)."""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
