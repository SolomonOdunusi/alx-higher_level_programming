#!/usr/bin/python3
"""Method that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds peak in unordered ints"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
