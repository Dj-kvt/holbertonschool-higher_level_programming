#!/usr/bin/python3
"""Writes a string to a text file and returns the number written."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number written."""
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
