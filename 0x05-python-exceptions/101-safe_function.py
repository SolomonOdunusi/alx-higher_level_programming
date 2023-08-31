#!/usr/bin/python3
"""
A func that executes a func safely
"""
import sys

def safe_function(fct, *args):
    try:
        return (fct(*args))
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
