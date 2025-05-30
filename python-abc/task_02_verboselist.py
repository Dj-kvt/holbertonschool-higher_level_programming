#!/usr/bin/env python3
"""Module for a verbose list class."""


class VerboseList(list):
    """A list that prints messages when modified."""
    
    def append(self, item):
        """Append an item to the list."""
        super().append(item)
        print(f"Added {item} to the list.")
    
    def extend(self, iterable):
        """Extend the list by appending elements from an iterable."""
        super().extend(iterable)
        print(f"Extended the list with {iterable}.")
    
    def remove(self, item):
        """Remove the first occurrence of an item from the list."""
        super().remove(item)
        print(f"Removed {item} from the list.")
    
    def pop(self, index=-1):
        """Remove and return an item at the given index (default last)."""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
