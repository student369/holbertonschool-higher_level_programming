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
    pas = [[1]]
    if not isinstance(n, int):
        raise TypeError("Must be a number")
    if n <= 0:
        return (list())
    for i in range(1, n):
        tmp = [1]
        last = pas[i - 1]
        for j in range(1, i):
            tmp.append(last[j] + last[j - 1])
        tmp.append(1)
        pas.append(tmp)
    return (pas)
