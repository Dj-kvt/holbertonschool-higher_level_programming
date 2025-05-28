#!/usr/bin/python3
"""Module that defines a function to check if an object"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class or a subclass."""
    return isinstance(obj, a_class) and type(obj) is not a_class
