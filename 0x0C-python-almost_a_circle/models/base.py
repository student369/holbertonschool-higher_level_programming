#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module Base

This module contains the Base class
"""


class Base(object):
    """Base class

    A simple empty Base class

    Arguments:
        nd_objects (int): Count the instances
            of this class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Returns a Base object

        Args:
            id (int): An id to this base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns a JSON format of the object"""
        a = list_dictionaries
        if a is None or len(a) == 0:
            return ("[]")
        if not isinstance(a, list):
            raise TypeError("must me a list of \
dicctionaries")
        import json
        return (json.dumps(a))
