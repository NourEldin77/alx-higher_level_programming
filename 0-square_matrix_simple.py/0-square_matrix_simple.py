#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list) and matrix:
        return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix))
