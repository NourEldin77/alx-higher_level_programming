#!/usr/bin/python3
""" say_my_name """


def say_my_name(first_name, last_name=""):
    """ print first and last name
    params:
        first_name: first_name string
        last_name: last_name string
    retrun:
        void
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name is not "":
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        print("My name is {:s}".format(first_name))
