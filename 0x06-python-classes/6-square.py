#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module Square

This module contains the Square class.
"""


class Square:
    """Square class

    A simple empty Square class.

    Attributes:
        size (int): The size if the Square.
        position (tuple): The Square position
    """

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor

        Args:
            size (int): The size of the Square.
            position (tuple): The Square position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """tuple: the size of the Square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        err = "position must be a tuple of 2 positive integers"
        if isinstance(value, tuple):
            if len(value) == 2 and value[0] >= 0 \
               and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError(err)
        else:
            raise TypeError(err)

    def area(self):
        """Area method

        This method calculare the are of this Square.
        """
        return (self.size * self.size)

    def my_print(self):
        """My print method

        This method print a Square based in the size
        setted previously.
        """
        if self.size == 0:
            print()
        else:
            for p0 in range(self.position[1]):
                print()
            for i in range(self.size):
                for p1 in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
