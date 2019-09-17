#!/usr/bin/python3
"""max_integer

Function to return the higher value of a list.
"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    hig = -1000
    for i in my_list:
        if i > hig:
            hig = i
    return (hig)
