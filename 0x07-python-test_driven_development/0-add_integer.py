#!/usr/bin/python3
""" simple module for add fun """


def add_integer(a, b=98):
    """ add two int
    :param: a
    :param: b
    :return: add
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an interger")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a) if type(a) is float else a
    b = int(b) if type(b) is float else b
    return (a + b)
