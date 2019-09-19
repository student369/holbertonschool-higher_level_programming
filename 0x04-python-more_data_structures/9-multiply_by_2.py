#!/usr/bin/python3
"""multiply_by_2

Function to multiply a dictionary by two
"""


def multiply_by_2(a_dictionary):
    return ({k: v * 2 for k, v in a_dictionary.items()})
