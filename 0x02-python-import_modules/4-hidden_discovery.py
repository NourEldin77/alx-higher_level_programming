#!/usr/bin/python3
""" ToDo: Doc """

if __name__ == "__main__":

    import hidden_4

    lst = dir(hidden_4)
    for ele in lst:
        if ele[0] == "_" and ele[1] == "_":
            continue
        else:
            print(ele)
