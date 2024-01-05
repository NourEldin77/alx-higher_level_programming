#!/usr/bin/python3
""" Simple Rectangle Class """


class Rectangle:
    """ simple Rectangle
    Atrributes:
        width: width of rectangle
        height: height of rectanle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ print bye when deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """ get the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ get the perimeter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """ print rectangle as info for end usr """
        count = 0
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            while count < self.__height:
                string += "#" * self.__width + "\n"
                count += 1
            return string.rstrip()

    def __repr__(self):
        """ print rectangle class string for debug or devepolper or eval"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
