#!/usr/bin/python3
"""no_c

Function to remove all characters c and C of a string.
"""


def no_c(my_string):
    string = ""
    for c in my_string:
        if c in ["c", "C"]:
            pass
        else:
            string += c
    return (string)
