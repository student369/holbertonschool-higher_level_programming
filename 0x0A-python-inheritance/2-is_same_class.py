#!/usr/bin/python3
""" Module 2-is_same_class

Module that contains the function is_same_class
that verify if its the exact class object.
"""


def is_same_class(obj, a_class):
    """ Returns True or False

    Arguments:
        obj (obj): A Python 3 object.
        a_class (cls): A Python 3 class.
    """
    return (type(obj) is a_class)
