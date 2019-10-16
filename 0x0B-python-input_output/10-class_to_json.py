#!/usr/bin/python3
""" Module 10-class_to_json

Module that contains the function class_to_json
that return a JSON from an class.
"""


def class_to_json(obj):
    """ Returns a representation in JSON of a class
    A function that get the JSON representation

    of a class.

    Args:
        obj (cls): The Python class
    """
    return (obj.__dict__)
