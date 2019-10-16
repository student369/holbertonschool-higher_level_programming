#!/usr/bin/python3
""" Module 3-write_file

Module that contains the function write_file
that write a text in the given filetext.
"""


def write_file(filename="", text=""):
    """ Returns The numbers of characters written

    A function that write a text and returns he
    characters printed.

    Args:
        filename (str): The filename of the file.
        text (str): The text to write
    """
    i = 0
    if not isinstance(filename, str):
        raise TypeError("It's not a valid filename.")
    if not isinstance(text, str):
        raise TypeError("It's not a valid text.")
    with open(filename, mode="w", encoding="utf-8") as f:
        i = f.write(text)
    return (i)
