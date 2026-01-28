#!/usr/bin/python3
"""Defines a Square class with size and position handling."""


class Square:
    """Represents a square with a given size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance.

        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square after validation.

        Args:
            value (int): New size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square after validation.

        Args:
            value (tuple): New position of the square.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
