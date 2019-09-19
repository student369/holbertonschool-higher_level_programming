#!/usr/bin/python3
"""square_matrix_simple

Function to compute square values in a matrix.
"""


def square_matrix_simple(matrix=[]):
    return ([[x * x for x in row] for row in matrix])
