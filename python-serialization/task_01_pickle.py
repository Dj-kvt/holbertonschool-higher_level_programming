#!/usr/bin/env python3
"""Basic serialization example using Pickle."""
import pickle
import os


class CustomObject:
    """A custom object to demonstrate serialization."""
    def __init__(self, name, age, is_student):
        """Initialize the custom object."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's information."""
        print(f"Name: {self.name}\nAge: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the object from a file."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} does not exist.")
        with open(filename, 'rb') as file:
            return pickle.load(file)
