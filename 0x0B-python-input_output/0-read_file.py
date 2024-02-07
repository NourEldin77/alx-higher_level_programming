#!/usr/bin/python3
""" read file module """


def read_file(filename=""):
    """ readfile and print to stdout """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
