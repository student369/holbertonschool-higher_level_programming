#!/usr/bin/python3
"""weight_average

Function to get the weight average
"""


def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    result = sum(n for _, n in my_list)
    avg = sum((x * (y / result)) for x, y in my_list)
    return (avg)
