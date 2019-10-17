#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 100-my_int

This module contains the MyInt class
that inherits from int and have
the operators inverted == !=
"""


class MyInt(int):
    """MyInt class

    A simple MyInt class
    """

    def __init__(self, value):
        """Returns an instance of a Rectangle

        Args:
            value (int): The value of this class
        """
        if isinstance(value, int):
            self.__int = value

    def __ne__(self, value):
        """Returns True"""
        return (True)

    def __eq__(self, value):
        """Returns False"""
        return (False)
