#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if isinstance(my_list, list) and my_list:
        return [True if num % 2 == 0 else False for num in my_list]
