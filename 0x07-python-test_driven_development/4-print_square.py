#!/usr/bin/python3
"""Module 4-print_square

This module contains the function print_square
"""


def print_square(size):
    """Returns nothing

    This method print a Square based in the size
    setted previously.

    Attributes:
        size (int): The size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        pass
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
