#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module Base

This module contains the Base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON format of the list"""
        a = list_dictionaries
        if a is None or len(a) == 0:
            return ("[]")
        if not isinstance(a, list):
            raise TypeError("must me a list of \
dicctionaries")
        return (json.dumps(a))

    @classmethod
    def save_to_file(cls, list_objs):
        """Return nothing

        Save a JSON representation of the object in a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            with open(filename, mode="x", encoding="utf-8") as f:
                pass
        lo = list()
        le = len(list_objs)
        for el in list_objs:
            lo.append(el.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(lo))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return (list())
        return (json.loads(json_string))
