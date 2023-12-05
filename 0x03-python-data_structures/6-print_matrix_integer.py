#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for i, array in enumerate(matrix):
            for y, element in enumerate(array):
                if y != 0:
                    print(" ", end='')
                print("{:d}".format(element), end="")
            print()
