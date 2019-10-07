#!/usr/bin/python3
""" Module 2-matrix_mul

Module that contains the function matrix_mul
"""


def matrix_mul(m_a, m_b):
    """ Returns a product matrix

    Arguments:
        m_a (list:int, list:float): First matrix
        m_b (list:int, list:float): Second matrix
    """
    res = []
    row_err = "Each row of the matrix must have the\
 same size"
    tp_err = "div must be a number"
    lt_erra = "m_a must be a list"
    lt_errb = "m_b must be a list"
    lt2d_erra = "m_a must be a list of lists"
    lt2d_errb = "m_b must be a list of lists"
    lt_emptya = "m_a can't be empty"
    lt_emptyb = "m_a can't be empty"
    lte_erra = "m_a should contain only integers or floats"
    lte_errb = "m_b should contain only integers or floats"
    lte_sizera = "each row of m_a must be of the same size"
    lte_sizerb = "each row of m_b must be of the same size"
    mul_err = "m_a and m_b can't be multiplied"
    if not isinstance(m_a, list):
        raise TypeError(lt_erra)
    if not isinstance(m_b, list):
        raise TypeError(lt_errb)
    if m_a[0] is None or not isinstance(m_a[0], list):
        raise TypeError(lt2d_erra)
    if m_b[0] is None or not isinstance(m_b[0], list):
        raise TypeError(lt2d_errb)
    if m_a == [] or m_a == [[]]:
        raise ValueError(lt_emptya)
    if m_b == [] or m_b == [[]]:
        raise ValueError(lt_emptyb)
    lenr0, lenc0 = len(m_a), len(m_a[0])
    i, j = 0, 0
    typ = None
    for i in range(lenr0):
        for j in range(lenc0):
            if i == 0 and j == 0:
                if isinstance(m_a[i][j], int):
                    typ = int
                elif isinstance(m_a[i][j], float):
                    typ = float
                else:
                    raise TypeError(lte_erra)
            else:
                if isinstance(m_a[i][j], typ):
                    continue
                else:
                    raise TypeError(lte_erra)
    lenr0, lenc0 = len(m_b), len(m_b[0])
    i, j = 0, 0
    typ = None
    for i in range(lenr0):
        for j in range(lenc0):
            if i == 0 and j == 0:
                if isinstance(m_b[i][j], int):
                    typ = int
                elif isinstance(m_b[i][j], float):
                    typ = float
                else:
                    raise TypeError(lte_erra)
            else:
                if isinstance(m_b[i][j], typ):
                    continue
                else:
                    raise TypeError(lte_errb)
    lenr0, lenc0 = len(m_a), len(m_a[0])
    n = lenr0
    i, j, cs = 0, 0, 0
    for i in range(lenr0):
        for j in range(lenc0):
            if len(m_a[i]) != lenc0:
                raise TypeError(lte_sizera)
    lenr0, lenc0 = len(m_b), len(m_b[0])
    p = lenc0
    i, j, cs = 0, 0, 0
    for i in range(lenr0):
        for j in range(lenc0):
            if len(m_b[i]) != lenc0:
                raise TypeError(lte_sizerb)
    lenr0, lenc0 = len(m_b), len(m_b[0])
    i, k, cs = 0, 0, 0
    for i in range(n):
        row = []
        cs = 0
        for k in range(p):
            try:
                cs += m_a[i][k] * m_b[k][j]
                row.append(cs)
            except ValueError:
                raise ValueError(mul_err)
        res.append(row)
    return (res)
