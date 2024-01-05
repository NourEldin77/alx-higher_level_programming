#!/usr/bin/python3
"""LockedClass that prevents from dynamically creating instance attributes"""


class LockedClass:
    """ Attributes:
    first_name
    """
    __slots__ = ["first_name"]
