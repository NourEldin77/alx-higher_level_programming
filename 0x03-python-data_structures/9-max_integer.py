#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list) and my_list:
        bigger = my_list[0]
        for num in my_list[1:]:
            bigger = num if num > bigger else bigger
        return bigger
    else:
        return None
