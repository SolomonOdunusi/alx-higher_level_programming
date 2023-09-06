#!/usr/bin/python3
"""Magic string"""


def magic_string():
    """Prints BestSchool multiple times."""
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ("BestSchool, " * (magic_string.count - 1) + "BestSchool")
