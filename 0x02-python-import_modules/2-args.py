#!/usr/bin/python3
""" ToDo: Doc"""


import sys

if __name__ == "__main__":
    argv_len = len(sys.argv)
    if argv_len == 1:
        print("0 arguments.")
    elif argv_len == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argv_len - 1))
        for i in range(1, argv_len):
            print("{}: {}".format(i, sys.argv[i]))
