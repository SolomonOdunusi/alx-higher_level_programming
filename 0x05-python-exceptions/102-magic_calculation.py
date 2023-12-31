#!/usr/bin/python3
"""
Create a function similar to the provided bytecode
"""


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception as e:
            result = b + a
            break
        finally:
            return (result)
