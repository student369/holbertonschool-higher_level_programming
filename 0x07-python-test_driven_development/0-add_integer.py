#!/usr/bin/python3
""" Module add_integer

Module that contains the function add_integer
that adds two numbers given.
"""


def add_integer(a, b=98):
    """ Returns a + b

    Arguments:
        a (int, float): The first number to sum
        b (int, float): The second number to to sum
    """
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
