#!/usr/bin/python3
""" Module 100-lazy_matrix_mul

Module that contains the function lazy_matrix_mul
"""


def lazy_matrix_mul(m_a, m_b):
    """ Returns a new product matrix

    Arguments:
        m_a (list:int, list:float): A first matrix of numbers
        m_b (list:int, list:float): A second matrix of numbers
    """
    import numpy as np
    err_lista = "m_a must be a list"
    err_listb = "m_b must be a list"
    err_lst2a = "m_a must be a list of lists"
    err_lst2b = "m_b must be a list of lists"
    err_emptya = "m_a can't be empty"
    err_emptyb = "m_b can't be empty"
    err_typea = "m_a should contain only integers or floats"
    err_typeb = "m_b should contain only integers or floats"
    err_sizea = "each row of m_a must be of the same size"
    err_sizeb = "each row of m_b must be of the same size"
    err_mul = "m_a and m_b can't be multipled:"
    if not isinstance(m_a, list):
        raise TypeError(err_lista)
    if not isinstance(m_b, list):
        raise TypeError(err_listb)
    if m_a == [] or m_a == [[]]:
        raise TypeError(err_emptya)
    if m_b == [] or m_b == [[]]:
        raise TypeError(err_emptyb)
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError(err_lst2a)
        if len(i) != len(m_a[0]):
            raise TypeError(err_sizea)
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError(err_lst2b)
        if len(i) != len(m_b[0]):
            raise TypeError(err_sizeb)
    i, j, lr, lc = 0, 0, len(m_a), len(m_a[0])
    typ = None
    for i in range(lr):
        for j in range(lc):
            if i == 0 and j == 0:
                if isinstance(m_a[i][j], int):
                    typ = int
                elif isinstance(m_a[i][j], float):
                    typ = float
                else:
                    raise TypeError(err_typea)
            else:
                if not isinstance(m_a[i][j], typ):
                    raise TypeError(err_typea)
    i, j, lr, lc = 0, 0, len(m_b), len(m_b[0])
    typ = None
    for i in range(lr):
        for j in range(lc):
            if i == 0 and j == 0:
                if isinstance(m_b[i][j], int):
                    typ = int
                elif isinstance(m_b[i][j], float):
                    typ = float
                else:
                    raise TypeError(err_typeb)
            else:
                if not isinstance(m_b[i][j], typ):
                    raise TypeError(err_typeb)
    A, B = np.array(m_a), np.array(m_b)
    C = A.dot(B)
    return (C)
