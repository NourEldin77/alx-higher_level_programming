#!/usr/bin/python3
""" divide matrix on number """


def matrix_divided(matrix, div):
    """ divide all element of matrix on div number
    params:
        matrix: list of list of integers of floats
        div: integer or float
    return:
        divided matrix
    """
    err_txt = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(err_txt)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err_txt)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(err_txt)
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    divided_matrix = []
    for row in matrix:
        divded_row = []
        for num in row:
            divded_row.append(round(num / div, 2))
        divided_matrix.append(divded_row)
    return (divided_matrix)
