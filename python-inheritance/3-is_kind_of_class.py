#!/usr/bin/python3
"""Module that defines a function to check if an object"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a specified class or subclasses."""
    return isinstance(obj, a_class)
