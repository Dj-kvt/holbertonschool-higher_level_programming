#!/usr/bin/env python3
"""Dragon class that can swim and fly."""


class SwimMixin:
    def swim(self):
        """The creature can swim!"""
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        """The creature can fly!"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """The dragon can roar!"""
        print("The dragon roars!")
