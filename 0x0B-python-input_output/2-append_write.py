#!/usr/bin/python3
def append_write(filename="", text=""):
    """the func appends a string at the end of a text file (UTF8)"""
    with open(filename, mode='a', encoding="utf-8") as f:
        appends_file = f.write(text)
        return (appends_file)
