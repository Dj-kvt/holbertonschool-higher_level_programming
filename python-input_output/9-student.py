#!/usr/bin/python3
"""Student module"""

Myclass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of Student instance"""
        return class_to_json(self)
    
    def __str__(self):
        """Return string representation of Student instance"""
        return "[Student] {} {} - {}".format(self.first_name, self.last_name, self.age)
