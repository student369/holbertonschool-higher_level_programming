#!/usr/bin/python3
""" Module 2-is_kind_of_class

Module that contains the function is_kind_of_class
that verify if is an instance
"""


def is_kind_of_class(obj, a_class):
    """ Returns True or False

    Arguments:
        obj (obj): A Python 3 object.
        a_class (cls): A Python 3 class.
    """
    return (isinstance(obj, a_class))
