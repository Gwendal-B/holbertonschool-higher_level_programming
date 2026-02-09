#!/usr/bin/python3
"""Defines a Student class with JSON serialization"""


class Student:
    """Represent a student whit first name, last name and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize student with names and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student"""
        return self.__dict__
