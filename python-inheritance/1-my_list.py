#!/usr/bin/python3
"""Define a class MyList that inherits from list and adds."""


class MyList(list):
    """Represent a list that can print its elements in sorted order."""

    def print_sorted(self):
        """Print the list in sorted order."""
        print("{}".format(sorted(self)))
