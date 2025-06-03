#!/usr/bin/python3
"""Defines a class_to_json function that returns the dictionary description
without any instance-specific attributes."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.
    """
    return obj.__dict__ if hasattr(obj, "__dict__") else obj.__class__.__dict__
