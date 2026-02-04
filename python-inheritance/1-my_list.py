#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class that can print itself sorted."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        new_list = self[:]
        new_list.sort()
        print(new_list)
