#!/usr/bin/python3
"""replace_in_list
Function to replace an element in the list.
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)
