#!/usr/bin/python3
"""uniq_add

Function to adds the unique integers.
"""


def uniq_add(my_list=[]):
    integers = set(my_list)
    sum = 0
    for i in integers:
        sum = sum + i
    return (sum)
