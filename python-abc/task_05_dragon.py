#!/usr/bin/env python3
"""Dragon class that defines a mystical creature."""


from abc import ABC, abstractmethod


class MysticalCreature(ABC):
    @abstractmethod
    def speak(self):
        """Make the creature speak."""
        pass

    @abstractmethod
    def move(self):
        """Make the creature move."""
        pass


class Dragon(MysticalCreature):
    def speak(self):
        """Make the dragon roar."""
        print("The dragon roars with ancient power!")

    def move(self):
        """Make the dragon fly majestically."""
        print("The dragon soars through the skies!")
