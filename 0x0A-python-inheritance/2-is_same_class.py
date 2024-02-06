#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """ see if obj isinstance of class"""
    return True if type(obj) is a_class else False
