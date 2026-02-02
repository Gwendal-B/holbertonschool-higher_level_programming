#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value.

        Args:
            name (str): name of the value
            value (int): value to validate
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
