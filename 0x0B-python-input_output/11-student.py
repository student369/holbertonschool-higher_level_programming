#!/usr/bin/python3
""" Module 11-student.py

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

    def to_json(self):
        """Return the JSON format of a student"""
        return (self.__dict__)
