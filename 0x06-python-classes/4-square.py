#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module Square

This module contains the Square class
"""


class Square:
    """Square class

    A simple empty Square class

    Attributes:
        size (int): The size if the Square
    """

    def __init__(self, size=0):
        """Square constructor

        Args:
            size (int): The size of the Square
        """
        self.size = size

    @property
    def size(self):
        """int: the size of the Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise ValueError("size must be an integer")

    def area(self):
        """Area method

        This method calculare the are of this Square
        """
        return (self.size * self.size)
