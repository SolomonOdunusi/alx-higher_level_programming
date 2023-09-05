#!/usr/bin/python3
"""Module for Rectangle with width and height"""


class Rectangle:
    """Rectangle class"""
    

    print_symbol = "#"
    number_of_instances = 0


    def __init__(self, width=0, height=0):
        """init function"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
    def area(self):
        """area function"""
        return (self.__width * self.__height)
    def perimeter(self):
        """perimeter function"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    def __str__(self):
        """str function"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec_array = []
        for i in range(self.__height):
            [rec_array.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rec_array.append("\n")
        return ("".join(rec_array))
    def __repr__(self):
        """repr function"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
    def __del__(self):
        """del function"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
