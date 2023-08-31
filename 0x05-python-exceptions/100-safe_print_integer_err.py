#!/usr/bin/python3
"""
safe_print_integer_err - prints an integer
@value: integer to print
Return: returns either True or False
"""


def safe_print_integer_err(value) -> bool:
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
