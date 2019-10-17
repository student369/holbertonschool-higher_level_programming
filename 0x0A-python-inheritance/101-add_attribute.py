#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 100-my_int

This module contains the add_atribute function
"""


def add_attribute(obj, name, value):
    """Returns Nothing

    A simple function to set atributes
    in a object.
    """
    if str(type(obj)).find("__main__") != -1:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
