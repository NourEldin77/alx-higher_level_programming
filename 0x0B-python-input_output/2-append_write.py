#!/usr/bin/python3
""" append_write module """


def append_write(filename="", text=""):
    """ appends a string at the end of text file
    return num of chars"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
