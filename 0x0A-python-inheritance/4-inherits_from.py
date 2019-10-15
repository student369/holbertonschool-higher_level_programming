#!/usr/bin/python3
""" Module 4-inherits_from

Module that contains the function inherits_from
that verify if the object inherits from the
given class.
"""


def inherits_from(obj, a_class):
    """ Returns True or False

    Arguments:
        obj (obj): A Python 3 object.
        a_class (cls): A Python 3 class.
    """
    if issubclass(obj.__class__, a_class) and\
       obj.__class__ is not a_class:
        return (True)
    else:
        return (False)
