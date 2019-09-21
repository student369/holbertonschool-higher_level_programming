#!/usr/bin/python3
"""square_matrix_map

Function to get the square using map.
"""


def square_matrix_map(matrix=[]):
    return (list(map(lambda r: list(map(lambda x: x * x, r)), matrix)))
