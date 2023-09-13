#!/usr/bin/python3
"""
the module writes a string to a text and num
"""


def write_file(filename="", text=""):
    """Write a string to a text file and returns the number"""
    with open(filename, mode='w', encoding="utf-8") as f:
        writes_file = f.write(text)
        return (writes_file)
