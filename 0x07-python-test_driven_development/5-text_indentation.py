#!/usr/bin/python3
"""Module 4-text_indentation

This module contains the function text_indentation
"""


def text_indentation(text):
    """Returns nothing

    This method prints a separated string in a new
    lines if finish in . : or ?.

    Attributes:
        text (str): The text to split
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    el = False
    txt_len = len(text)
    for i in range(txt_len):
        if text[i] == "." or text[i] == "?" or\
           text[i] == ":":
            print("{:s}".format(text[i]), end="\n\n")
            el = True
        else:
            if text[i] == " " and el:
                continue
            else:
                el = False
                print("{:s}".format(text[i]), end="")
