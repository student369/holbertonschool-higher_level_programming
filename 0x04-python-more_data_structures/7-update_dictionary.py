#!/usr/bin/python3
"""update_dictionary

Function to replace or add key/val in the dictionary
"""


def update_dictionary(a_dictionary, key, value):
    k = str(key)
    if k in a_dictionary.keys():
        a_dictionary[k] = value
        return (a_dictionary)
    else:
        a_dictionary.update({k: value})
        return (a_dictionary)
