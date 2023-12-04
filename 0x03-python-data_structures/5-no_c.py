#!/usr/bin/python3
def no_c(my_string):
    if len(my_string):
        table = str.maketrans({ord('C'): None, ord('c'): None})
        no_c_string = my_string.translate(table)
        return no_c_string
