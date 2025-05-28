#!/usr/bin/python3
"""Module that defines a function to check if an object"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class."""
    return type(obj) is a_class
