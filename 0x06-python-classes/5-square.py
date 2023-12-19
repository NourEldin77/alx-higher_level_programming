#!/usr/bin/python3
""" square class """


class Square:

    """ simple square
    Atrributes:
        size: size of square
    """
    def __init__(self, size=0):
        """ init the size """
        self.size = size

    def area(self):
        """ area of square """
        return self.__size ** 2

    @property
    def size(self):
        """ getter size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter size """
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        """ print the square """
        count = 0
        if self.__size == 0:
            print()
        else:
            while count < self.__size:
                print("#" * self.__size)
                count += 1
