#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module Base

This module contains the Base class
"""
import json
import turtle
from tkinter import *


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
        for el in list_objs:
            lo.append(el.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(lo))

    @staticmethod
    def from_json_string(json_string):
        """Return an object from the json string"""
        if json_string is None or len(json_string) == 0:
            return (list())
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of the class"""
        from models import rectangle as r
        ret = r.Rectangle(1, 1)
        ret.update(**dictionary)
        return (ret)

    @classmethod
    def load_from_file(cls):
        """Returns an object from a JSON string

        A function that get the Python object
        from the JSON string in an textfile.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                pass
        except IOError:
            return (list())
        with open(filename, mode="r", encoding="utf-8") as f:
            ret = list()
            lst = Base.from_json_string(f.read())
            for ins in lst:
                ret.append(Base.create(**ins))
            return (ret)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Return nothing

        A function to draw rectangles amd
        squares in the screen
        """
        if list_rectangles is not None\
           and len(list_rectangles) > 0:
            for r in list_rectangles:
                t = turtle.Turtle()
                t.penup()
                t.goto(r.x, r.y)
                t.pendown()
                t.forward(r.width)
                t.right(90)
                t.forward(r.height)
                t.right(90)
                t.forward(r.width)
                t.right(90)
                t.forward(r.height)
        if list_squares is not None\
           and len(list_squares) > 0:
            for s in list_squares:
                t = turtle.Turtle()
                t.penup()
                t.goto(s.x, s.y)
                t.pendown()
                t.forward(s.size)
                t.right(90)
                t.forward(s.size)
                t.right(90)
                t.forward(s.size)
                t.right(90)
                t.forward(s.size)
