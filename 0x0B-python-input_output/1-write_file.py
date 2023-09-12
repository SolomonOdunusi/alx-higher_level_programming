#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        writes_file = f.write(text)
        return (writes_file)
