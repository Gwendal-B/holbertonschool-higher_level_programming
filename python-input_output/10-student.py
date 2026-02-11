#!/usr/bin/python3
"""Defines a Student class with JSON serialization and attribute filtering"""


class Student:
    """Represent a student whit first name, last name and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize student with names and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.

        If attrs is a list of strings, only attributes in this list are
        included.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return{
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__
