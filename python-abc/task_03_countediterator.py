#!/usr/bin/env python3
"""CountedIterator class that counts the number iterable."""


class CountedIterator:
    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item from the iterator and increment the count."""
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def get_count(self):
        """Return the number of items iterated over."""
        return self.count
