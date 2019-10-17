#!/usr/bin/python3
""" Module 12-student.py

Module that contains the class Student
and a methods
"""


class Student(object):
    """ Student class

    A simple Student class.

    Attributes:
        first_name (str): The student first name
        last_name (str): The student last name
        age (int): The student age
    """

    def __init__(self, first_name, last_name, age):
        """Return a student object

        Args:
            first_name (str): The student first name
            last_name (str): The student last name
            age (int): The student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the JSON format of a student

        Args:
            attrs: (list of str): A list of
                specific attributes
        """
        ndic = dict()
        if attrs is None:
            return self.__dict__
        for key in attrs:
            if hasattr(self, key):
                ndic[key] = getattr(self, key)
        return (ndic)

    def reload_from_json(self, json):
        """Return Nothing

        Reload the instance based in the json
        given.
        """
        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)
