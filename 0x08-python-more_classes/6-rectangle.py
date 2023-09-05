#!/usr/bin/python3
"""Module that defines a rectangle for 6-rectangle.py with #"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    @property
    def width(self):
        """Get width of a rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """Set width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """Get height of a rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """Set height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """Return area of a rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        """Return perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)
    def __str__(self):
        """Print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)
    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        """Delete a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
