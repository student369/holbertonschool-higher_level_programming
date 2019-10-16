#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 10-square.py

This module contains the Rectangle class
that inherits the BaseGeometry class.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class

    A simple Square class
    """

    def __init__(self, size):
        """Returns an instance of a Rectangle

        Args:
            size (int): The size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the Square area"""
        return (self.__size ** 2)

    def __repr__(self):
        return ("[Rectangle] {:s}/{:s}"
                .format(str(self.__size),
                        str(self.__size)))
