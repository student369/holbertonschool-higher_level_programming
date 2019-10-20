#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module rectangle

This module contains the Rectangle class
"""
from models import base


class Rectangle(base.Base):
    """Rectangle class

    A simple Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Returns a Rectangle object

        Args:
            width (int): The rectangle width
            height (int): The rectangle height
            x (int, optional): The x position
            y (int, optional): The y position
            id (int, optional): The id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """int: The width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The x pos of the rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The y pos of the rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return (self.width * self.height)

    def display(self):
        """Returns nothing

        This method print a Square based in the higth
        and width given previously.
        """
        import sys
        if self.y > 0:
            for nl in range(self.y):
                print("\n", end="", file=sys.stdout)
        for i in range(self.height):
            if self.x > 0:
                for s in range(self.x):
                    print(" ", end="",
                          file=sys.stdout)
            for j in range(self.width):
                print("#", end="", file=sys.stdout)
            print(file=sys.stdout)

    def __str__(self):
        """Returns an string format of the Rectangle"""
        return ("[Rectangle] ({:s}) {:s}/{:s} - {:s}/{:s}"
                .format(
                    str(self.id), str(self.x),
                    str(self.y), str(self.width),
                    str(self.height)))
