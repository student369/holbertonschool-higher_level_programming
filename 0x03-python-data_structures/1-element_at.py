#!/usr/bin/python3
"""element_at
Function to get an elemen of a list.
"""


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return (None)
    return (my_list[idx])
