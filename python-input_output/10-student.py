#!/usr/bin/python3
"""Student module"""


class Student(Myclass):
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                return {attr: getattr(self, attr) for attr in attrs if hasattr(
                    self, attr)}
        return self.__dict__
