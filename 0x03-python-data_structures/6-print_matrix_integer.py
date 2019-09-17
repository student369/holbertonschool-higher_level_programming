#!/usr/bin/python3
"""print_matrix_integer

Function to print a matrix of numbers.
"""


def print_matrix_integer(matrix=[[]]):
    rows, cols = len(matrix), len(matrix[0])
    if rows > 0 and cols > 0:
        for r in range(rows):
            for c in range(cols):
                if c == (cols - 1):
                    print("{:d}".format(matrix[r][c]))
                else:
                    print("{:d} ".format(matrix[r][c]), end="")
    else:
        print("{}".format(""))
