#!/usr/bin/env python3
"""Basic serialization example using JSON."""
import json

def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save it to a file."""
    with open (filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load data from a JSON file and deserialize it."""
    with open(filename, 'r') as file:
        return json.load(file)
