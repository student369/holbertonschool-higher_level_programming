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

        if attrs is not None:
            if not isinstance(attrs, list):
                raise TypeError("must be a list")
            ndic = dict()
            cdic = self.__dict__
            attrs = sorted(attrs)
            for k in attrs:
                if k in cdic.keys():
                    ndic.__setitem__(k, cdic[k])
            return (ndic)
        return (sorted(self.__dict__))
