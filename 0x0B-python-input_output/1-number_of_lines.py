#!/usr/bin/python3
""" Module 1-number_of_lines

Module that contains the function number_of_lines
that count the number of lines of a text file.
"""


def number_of_lines(filename=""):
    """ Returns The numbers of lines of a filename.

    A function to get the number of lines of a text.

    Args:
        filename (str): The filename of the file.
    """
    i = 0
    if not isinstance(filename, str):
        raise TypeError("It's not a valid filename.")
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            i = i + 1
    return (i)
