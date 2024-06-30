#!/usr/bin/python3


""" ToDo: Doc """


import sys

if __name__ == "__main__":
    argv_len = len(sys.argv)
    if argv_len < 2:
        print(0)
    else:
        sum = 0
        for i in range(1, argv_len):
            sum += int(sys.argv[i])
        print(sum)
