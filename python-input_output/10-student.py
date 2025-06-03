#!/usr/bin/python3
"""Student module"""
Myclass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json


class Student(Myclass):
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize Student instance"""
        super().__init__(first_name)
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student instance"""
        if attrs is None:
            return class_to_json(self)
        else:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
