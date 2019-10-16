#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 5-base_geometry

This module contains the BaseGeometry class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class

    A simple empty Rectangle class
    """

    def __init__(self, width, height):
        """Returns an instance of a Rectangle

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
