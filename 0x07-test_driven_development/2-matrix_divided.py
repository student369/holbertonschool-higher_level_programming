#!/usr/bin/python3
""" Module 2-matrix_divided

Module that contains the function matrix_divided
"""


def matrix_divided(matrix, div):
    """ Returns a new matrix with the divisions

    Arguments:
        matrix (list): A matrix of numbers
        b (int, float): The second number to to divide
    """
    res = []
    row_err = "Each row of the matrix must have the\
 same size"
    tp_err = "div must be a number"
    lt_err = "matrix must be a matrix (list of lists)\
 of integers/floats"
    if not isinstance(div, int):
        if not isinstance(div, float):
            raise TypeError(tp_err)
    typ = None
    lenr, lenc = len(matrix), len(matrix[0])
    for s in range(lenr):
        if len(matrix[s]) != lenc:
            raise TypeError(row_err)
    for i in range(lenr):
        row = []
        for j in range(lenc):
            if i == 0 and j == 0:
                if isinstance(matrix[i][j], int):
                    typ = int
                    row.append(
                        round((matrix[i][j] / div), 2))
                elif isinstance(matrix[i][j], float):
                    typ = float
                    row.append(
                        round((matrix[i][j] / div), 2))
                else:
                    raise TypeError(lt_err)
            else:
                if isinstance(matrix[i][j], typ):
                    row.append(
                        round((matrix[i][j] / div), 2))
                else:
                    raise TypeError(lt_err)
        res.append(row)
    return (res)
