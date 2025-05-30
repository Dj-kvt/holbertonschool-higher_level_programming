#!/usr/bin/env python3
"""Module that defines an abstract base class and its subclasses."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Woof!"


class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow!"
