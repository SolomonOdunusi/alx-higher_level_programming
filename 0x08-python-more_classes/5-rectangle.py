#!/usr/bin/python3
"""Module for Rectangle with width and height"""


class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        """the init function"""
        self.width = width
        self.height = height
    @property
    def width(self):
        """the width getter"""
        return (self.__width)
    @width.setter
    def width(self, value):
        """the width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height getter"""
        return (self.__height)
    @height.setter
    def height(self, value):
        """the height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area function"""
        return (self.__width * self.__height)
    def perimeter(self):
        """the perimeter function"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    def __str__(self):
        """the str function"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return (("#" * self.__width + "\n") * self.__height)[:-1]
    def __repr__(self):
        """the repr function"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
    def __del__(self):
        """the del function"""
        print("Bye rectangle...")
        return
