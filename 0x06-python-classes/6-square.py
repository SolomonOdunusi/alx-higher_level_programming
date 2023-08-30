#!/usr/bin/python3
"""
Defines a class Square that defines a square with
private instance attribute size and position
def __init__(self, size=0, position=(0, 0)):
def size(self):
def size(self, value):
def position(self):
def position(self, value):
def area(self):
def my_print(self):
"""


class Square:
    """A class that defines a square by size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square with a size and position"""
        """Args: size (int): size of Square"""
        """position (tuple): position of Square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        """Args: value (tuple): position of Square"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
