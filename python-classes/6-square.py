#!/usr/bin/python3
"""Module 6-square
Defines a class Square with size and position.
"""


class Square:
    """Class representing a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(v, int) for v in value) or
            not all(v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' at the correct position."""
        if self.__size == 0:
            print()
            return

        # Print vertical position (newlines)
        for _ in range(self.__position[1]):
            print()

        # Print each line of the square with horizontal spaces
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
