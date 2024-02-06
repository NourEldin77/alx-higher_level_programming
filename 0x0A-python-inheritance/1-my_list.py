#!/usr/bin/python3
""" My_list module """


class MyList(list):
    """ class that inherits form list """
    def print_sorted(self):
        for ele in self:
            if type(ele) is not int:
                raise TypeError("all elements must be of type int")
        sorted_array = sorted(self)
        print(sorted_array)
