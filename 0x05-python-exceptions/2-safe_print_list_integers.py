#!/usr/bin/python3
"""
Contains a function that prints the first x elements of a list and only
integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    j = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            j += 1
        except (TypeError, ValueError):
            continue
    print()
    return (j)
