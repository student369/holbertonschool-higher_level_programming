#!/usr/bin/python3
"""print_sorted_dictionary

Function to prints the dictionary with keys ordered.
"""


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return (None)
    keys_ordered = sorted(list(a_dictionary.keys()))
    for k in keys_ordered:
        print("{:s}: {}".format(k, a_dictionary[k]))
