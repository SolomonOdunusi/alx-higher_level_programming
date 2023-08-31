#!/usr/bin/python3
"""
The func prints with boolen return value
"""


def safe_print_integer(value) -> bool:
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
