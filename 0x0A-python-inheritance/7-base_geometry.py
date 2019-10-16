#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 7-base_geometry

This module contains the BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry class

    A simple empty BaseGeometry class
    """

    def area(self):
        """Returns an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Returns a TypeError or ValuError exception

        Args:
            name (str): The
        """
        if not isinstance(name, str):
            raise TypeError("The first parameter must \
be an string")
        if not isinstance(value, int) or\
           value.__class__ is bool:
            raise TypeError("{:s} must be an integer"
                            .format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater tha\
n 0".format(name))
