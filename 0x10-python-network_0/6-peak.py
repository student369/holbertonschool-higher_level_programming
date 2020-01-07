#!/usr/bin/python3
""" Module 6-peak

Function to find the peak number
"""


def find_peak(list_of_integers):
    """ Returns the peak number

    Function to find the peak number

    Args:
        list_of_integers (list): The numners list.
    """
    if list_of_integers == []:
        return (None)
    mx = list_of_integers[0]
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > mx:
            mx = list_of_integers[i]
    return (mx)
