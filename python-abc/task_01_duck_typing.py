#!/usr/bin/env python3
"""Duck typing example with Circle and Rectangle classes."""
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return 3.14159 * (self.__radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * 3.14159 * self.__radius

    def __str__(self):
        """Return a string representation of the circle."""
        return "[Circle] Radius: {}".format(self.__radius)


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] Width: {}, Height: {}".format(
            self.__width, self.__height)


def shape_info(shape):
    """Print information about the shape."""
    if isinstance(shape, Shape):
        print("Shape Info:")
        print("Area:", shape.area())
        print("Perimeter:", shape.perimeter())
        print(str(shape))
    else:
        print("Not a valid shape.")
