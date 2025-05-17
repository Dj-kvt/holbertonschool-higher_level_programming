#!/usr/bin/python3
"""
This module provides the add_integer function
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats, converting floats to integers.
    Raises TypeError if arguments are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt", optionflags=doctest.ELLIPSIS)
