#!/usr/bin/python3
"""complex_delete

Function to delete some keys of the dictionary
"""


def complex_delete(a_dictionary, value):
    ks = []
    for k, v in a_dictionary.items():
        if a_dictionary[k] == value:
            ks.append(k)
    for k in ks:
        del a_dictionary[k]
    return (a_dictionary)
