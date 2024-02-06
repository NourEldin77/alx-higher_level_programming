#!/usr/bin/python3
""" inherits_from module """


def inherits_from(obj, a_class):
    """ check if obj is instance of class that inherited"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
