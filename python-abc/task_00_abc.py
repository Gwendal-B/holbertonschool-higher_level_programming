#!/usr/bin/env python3
"""Module defining an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
