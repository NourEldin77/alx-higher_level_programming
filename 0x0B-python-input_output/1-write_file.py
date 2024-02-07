#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """ write a string to text file with UTF8 encoding """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
