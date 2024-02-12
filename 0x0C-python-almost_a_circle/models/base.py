#!/usr/bin/python3
""" BASE CLASS MODULE """


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor
            :param:
            id:
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
