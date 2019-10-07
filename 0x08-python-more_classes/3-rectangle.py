#!/usr/bin/python3
""" Module 3-rectangle

Module that contains the class Rectangle
and a methods
"""


class Rectangle:
    """ Rectangle class

    A empty Rectangle class.

    Attributes:
        width (int): The rectangle width
        height (int): The rectangle height
    """

    def __init__(self, width=0, height=0):
        """Return a rectangle object

        Args:
            width (int): The rectangle width
            height (int): The rectangle height                             """
        self.height = height
        self.width = width

    @property
    def width(self):
        """int: The width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return (self.height * self.width)

    def perimeter(self):
        """Return a rectangle perimeter"""
        if self.height == 0 or self.width == 0:
            return (0)
        return (2 * (self.height + self.width))

    def __str__(self):
        """Return a # character rectangle"""
        if self.height == 0 or self.width == 0:
            return ("")
        rec = ""
        for i in range(self.height):
            for j in range(self.width):
                rec = rec + "#"
            rec = rec + "\n"
        return(rec[:-1])
