#!/usr/bin/python3
"""Converts a JSON string representation to an object."""
import json

def from_json_string(my_str):
    """Returns the object represented by a JSON string."""
    return json.loads(my_str)
