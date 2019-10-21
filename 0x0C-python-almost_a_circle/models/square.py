#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module rectangle

This module contains the Square class
"""
from models import rectangle


class Square(rectangle.Rectangle):
    """Square class

    A simple Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Returns a Square object

        Args:
            size (int): The square size
            x (int, optional): The x position
            y (int, optional): The y position
            id (int, optional): The id
        """
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        """Returns an string format of the Rectangle"""
        return (
            "[Square] ({:s}) {:s}/{:s} - {:s}"
            .format(
                str(self.id), str(self.x),
                str(self.y), str(self.size)
            )
        )

    @property
    def size(self):
        """int: The width of the rectangle"""
        return (self.__width)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width, self.__height = (value, value)

    def update(self, *args, **kwargs):
        """Returns nothing

        This method update the parameters of
        the actual object.

        Args:
            args[0] (int, optional): The id
            args[1] (int): The square size
            args[2] (int, optional): The x position
            args[3] (int, optional): The y position
        """
        i = 0
        if args is not None and len(args) > 0:
            for arg in args:
                if i == 0:
                    self.__init__(
                        size=self.size,
                        id=arg
                    )
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                else:
                    break
                i = i + 1
        elif kwargs is not None and len(kwargs) > 0:
            for i, arg in kwargs.items():
                setattr(self, i, arg)

    def to_dictionary(self):
        """Return the dictionary version of this object"""
        dicver = dict()
        dicver.__setitem__("id", self.id)
        dicver.__setitem__("x", self.x)
        dicver.__setitem__("size", self.size)
        dicver.__setitem__("y", self.y)
        return (dicver)
