#!/usr/bin/python3
""" my_int module """


class MyInt(int):
    """ subclass from int """
    def __eq__(self, num):
        """ invert the eq """
        return super().__ne__(num)

    def __ne__(self, num):
        """ invert the ne """
        return super().__eq__(num)
