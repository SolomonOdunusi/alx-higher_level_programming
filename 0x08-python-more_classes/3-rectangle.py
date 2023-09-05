#!/usr/bin/python3
"""Module that defines a rectangle for 3-rectangle.py with #"""


class Rectangle:
    """Class that defines a rectangle with #"""
    def __init__(self, width=0, height=0):
        """Initializes the method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        """Initializes the method"""
        return self.__width * self.__height

    def perimeter(self):
        """Initializes the method"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
        
    def __str__(self):
        """Adds string hash"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (("#" * self.__width + "\n") * self.__height)[:-1]
