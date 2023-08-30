#!/usr/bin/python3
"""
Created a class called Square with
Private instance attribute
def __init__(self, size=0):
def size(self):
"""


class Square:
    """A class representing a square"""
    def __init__(self, size=0):
        """Initializes Square with a size"""
        """Args: size (int): size of Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)
