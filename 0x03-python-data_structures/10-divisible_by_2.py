#!/usr/bin/python3
"""divisible_by_2

Function to return the the even list
of the list given.
"""


def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
