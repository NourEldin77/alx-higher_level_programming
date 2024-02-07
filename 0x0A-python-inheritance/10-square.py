#!/usr/bin/python3
""" square module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square shape class """
    def __init__(self, size):
        """ instantiation the object """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ calc area of squar A^2 """
        return (self.__size ** 2)

    def __str__(self):
        """ print rectangle as info for end usr """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))

    def __repr__(self):
        """ print rectangle class info for programmer or eval """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
