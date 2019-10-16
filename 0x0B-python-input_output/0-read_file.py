#!/usr/bin/python3
""" Module 0-read_file

Module that contains the function def read_file
that read a file and print in stdout.
"""


def read_file(filename=""):
    """ Returns Nothing

    A function to reads a file and prints in the standar
    output.
    """
    if not isinstance(filename, str):
        raise TypeError("It's not a valid filename.")
    with open(filename) as f:
        print(f.read(), end="")
