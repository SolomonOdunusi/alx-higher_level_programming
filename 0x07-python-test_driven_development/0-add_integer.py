#!/usr/bin/python3

def add_integer(a, b=98):
    """Function that adds 2 integers.
    Args:
        a (int): first integer.
        b (int): second integer.

    Returns: int: sum of a and b.

    Raises:
        TypeError: if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('inf') or b == float('inf'):
        raise OverflowError("int too large to convert to float")
    return (int(a) + int(b))
