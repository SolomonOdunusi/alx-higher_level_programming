#!/usr/bin/python3
"""
Define a class Square with public instance method
def area(self) and def my_print(self)
"""


class Square:
    """A class that defines a square by size"""
    def __init__(self, size=0):
        """Initializes Square with a size"""
        """Args: size (int): size of Square"""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        """Args: value (int): size of Square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
