#!/usr/bin/python3
"""mutiply_list_map

Function to multiply the values of the dictionary in other way.
"""


def mutiply_list_map(my_list=[], number=0):
    return (list(map(lambda x: x * number, my_list)))
