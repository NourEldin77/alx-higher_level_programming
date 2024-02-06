#!/usr/bin/python3
""" base_geometry module """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ raise an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "check if value is integer and larger that 0"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater that 0".format(name))
