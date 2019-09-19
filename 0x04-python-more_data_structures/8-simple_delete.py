#!/usr/bin/python3
"""simple_delete

Function to delete a key in the dictionary.
"""


def simple_delete(a_dictionary, key=""):
    k = str(key)
    if k in a_dictionary.keys():
        del a_dictionary[k]
        return (a_dictionary)
    else:
        return (a_dictionary)
