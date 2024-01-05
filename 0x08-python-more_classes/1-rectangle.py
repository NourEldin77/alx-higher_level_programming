#!/usr/bin/python3
""" Simple Rectangle Class """


class Rectangle:
    """ simple Rectangle
    Atrributes:
        width: width of rectangle
        height: height of rectanle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height """
        if type(value) is int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
