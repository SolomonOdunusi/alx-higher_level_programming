#!/usr/bin/python3
"""
Contains a function that divides 2 integers and prints the result.
"""


def safe_print_division(a, b) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
