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
    li = list_of_integers
    if li == []:
        return (None)
    if len(li) == 1:
        return (li[0])
    if li[0] > li[len(li) -1]:
        return (find_peak(li[:(len(li) + 1)//2])
    else:
        return (find_peak(li[(len(li))//2:])
