#!/usr/bin/python3
"""best_score

Function to return the higher value of a list.
"""


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.values()) == 0:
        return (None)
    hig, name = -1000, ""
    for k, v in a_dictionary.items():
        if v > hig:
            name = k
    return (name)
