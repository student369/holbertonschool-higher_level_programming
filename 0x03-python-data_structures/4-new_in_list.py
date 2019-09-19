#!/usr/bin/python3
"""new_in_list

Function to replace an element of a copy of the list.
"""


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list.copy())
    cp = my_list.copy()
    cp[idx] = element
    return (cp)
