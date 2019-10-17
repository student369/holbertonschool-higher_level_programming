#!/usr/bin/python3
""" Module 14-pascal_triangle.py

Module that contains the function pascal_triangle
that
"""


def pascal_triangle(n):
    """ Returns A list of list of integers

    A function that returns a list of list of ingegers
    showing the Pascal triangle.
    """
    pasc = []
    tmp = None
    if not isinstance(n, int):
        raise TypeError("Must be a number")
    if n <= 0:
        return (pasc)
    for i in range(n):
        row = []
        for j in range(i + 1):
            val = 1
            if j >= 1 and j < (i + 1):
                val = tmp[j] + tmp[j - 1]
            row.append(val)
        if i >= 1:
            tmp = row
        pasc.append(row)
    return (pasc)
