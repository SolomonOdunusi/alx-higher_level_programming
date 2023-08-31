#!/usr/bin/python3
"""
A func that executes a func safely
"""


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
