#!/usr/bin/python3
""" Module 4-append_write

Module that contains the function append_write
that appends a text in the given filetext.
"""


def append_write(filename="", text=""):
    """ Returns The numbers of characters appends

    A function that apends a text and returns he
    characters written.

    Args:
        filename (str): The filename of the file.
        text (str): The text to write
    """
    i = 0
    if not isinstance(filename, str):
        raise TypeError("It's not a valid filename.")
    if not isinstance(text, str):
        raise TypeError("It's not a valid text.")
    with open(filename, mode="a", encoding="utf-8") as f:
        i = f.write(text)
    return (i)
