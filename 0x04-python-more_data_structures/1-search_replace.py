#!/usr/bin/python3
"""search_replace

Function to replace the elements in a list in another.
"""


def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] is search:
            new_list[i] = replace
    return (new_list)
