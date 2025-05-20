#!/usr/bin/python3

"""Square class that defines a square and calculates its area."""


class Square:

    """Class that defines a square."""
    def __init__(self, size=0):
        """Initialize the square with a size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
