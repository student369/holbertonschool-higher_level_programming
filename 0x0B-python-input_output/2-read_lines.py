#!/usr/bin/python3
""" Module 2-read_lines

Module that contains the function read_lines
that reads an specific number of lines
"""


def read_lines(filename="", nb_lines=0):
    """ Returns The numbers of lines of a filename.

    A function that reads an specific number of lines

    Args:
        filename (str): The filename of the file.
        nb_lines (int): The number of lines
    """
    i = 0
    if not isinstance(filename, str):
        raise TypeError("It's not a valid filename.")
    if not isinstance(nb_lines, int):
        raise TypeError("The number of lines must be a number.")
    if nb_lines < 0:
        raise ValueError("The number of lines must be greater\
ot equals to 0.")
    with open(filename, encoding="utf-8") as f:
        while True:
            line = f.readline()
            if nb_lines == 0:
                if not line:
                    break
            else:
                if not line or i == nb_lines:
                    break  
            print(line, end="")
            i = i + 1
    return (i)
