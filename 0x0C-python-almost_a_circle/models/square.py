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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns an string format of the Rectangle"""
        return (
            "[Square] ({:s}) {:s}/{:s} - {:s}"
            .format(
                str(self.id), str(self.x),
                str(self.y), str(self.width)
            )
        )
