#!/usr/bin/env python3
"""FlyingFish class that inherits from Fish and Bird classes."""


class Fish:
    def swim(self):
        """The fish can swim!"""
        print("The fish is swimming!")

    def habitat(self):
        """The fish lives in water."""
        print("The fish lives in water.")


class Bird:
    def fly(self):
        """The bird can fly!"""
        print("The bird is flying!")

    def habitat(self):
        """The bird lives in the sky."""
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """The FlyingFish class inherits from both Fish and Bird classes."""
    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        """The flying fish lives both in water and the sky!"""
        print("The flying fish lives both in water and the sky!")

    def fly(self):
        """The flying fish can fly!"""
        print("The flying fish is soaring!")
