#!/usr/bin/python3
"""Append a string to a text file and return the number of characters added."""

def append_write(filename="", text=""):
    """Append a string to a text file and return the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
