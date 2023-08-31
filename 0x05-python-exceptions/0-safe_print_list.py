#!/usr/bin/python3
"""
To create a safe func to print list
"""


def safe_print_list(my_list=[], x=0):
    """
    The func prints the elements of the list
    Args:
        my_list (list): A list of elements to be printed
        x (int): The number of elements to be printed
    Returns:
        int: returns an int with the number of elements printed
    """
    j = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            j += 1
    except IndexError:
        pass
    finally:
        print("")
    return (j)
