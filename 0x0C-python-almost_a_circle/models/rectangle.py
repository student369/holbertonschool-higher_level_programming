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
        """int: The width of the reactangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """int: The height of the reactangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """int: The x pos of the rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """int: The y pos of the rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = value
