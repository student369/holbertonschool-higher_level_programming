#!/usr/bin/python3
""" Module 0-rectangle

Module that contains the class Rectangle
"""


class Rectangle:
    """ Rectangle class

    A empty Rectangle class.

    Attributes:
        width (int): The rectangle width
        height (int): The rectangle height
    """

    def __init__(self, width=0, height=0):
        """ Return a rectangle object

        Args:
            width (int): The rectangle width
            height (int): The rectangle height                             """
        self.height = height
        self.width = width

    @property
    def width(self):
        """int: The width of the rectangle"""
        return self.__width

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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
