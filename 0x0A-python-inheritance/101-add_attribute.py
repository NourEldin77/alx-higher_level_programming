#!/usr/bin/python3
""" add_attribute module """


def add_attribute(obj, key, value):
    """ add new attribute to object """
    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("Can't add new attribute")
