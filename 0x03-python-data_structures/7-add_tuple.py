#!/usr/bin/python3
"""add_tuple

Function to adds two tuples.
"""


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    for i in range(2):
        try:
            val1 = tuple_a[i]
        except IndexError:
            val1 = 0
        try:
            val2 = tuple_b[i]
        except IndexError:
            val2 = 0
        new_tuple.append(val1 + val2)
    return (tuple(new_tuple))
