#!/usr/bin/python3
""" square class """


class Square:

    """ simple square
    Atrributes:
        size: size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ init the size """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ position getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ print the square """
        count = 0
        if self.__size == 0:
            print()
        else:
            while count < self.__size:
                print("#" * self.__size)
                count += 1
