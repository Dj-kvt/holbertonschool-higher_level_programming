#!/usr/bin/python3
"""BaseGeometry class that defines a base geometry."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Method that raises an Exception with a message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value as an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
