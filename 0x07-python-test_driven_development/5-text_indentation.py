#!/usr/bin/python3
"""Module 4-text_indentation

This module contains the function text_indentation
"""


def text_indentation(text):
    """Returns nothing

    This method prints a separated string in a new
    lines if finish in . or ?.

    Attributes:
        text (str): The text to split
    """
    if not isinstance(text, str):
        raise TypeError("text must be an string")
    find = 0
    txt_len = len(text)
    for i in range(txt_len):
        if text[i] == "." or text[i] == "?" or\
           text[i] == ":":
            print("{:s}".format(text[i]), end="\n\n")
            find = 1
        else:
            if text[i] == " " and find == 1:
                find = 0
            else:
                print("{:s}".format(text[i]), end="")
