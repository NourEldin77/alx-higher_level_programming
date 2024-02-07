#!/usr/bin/python3
""" rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ instantiation the object """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ get the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ print rectangle as info for end usr """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __repr__(self):
        """ print rectangle class info for programmer or eval """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
