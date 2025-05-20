#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:

    def __init__(self, size=0):
        """Initialize a new Square with a given size."""
        self.size = size  # on passe par le setter pour validation

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
