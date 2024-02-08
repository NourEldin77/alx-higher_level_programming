#!/usr/bin/python3
""" student class module """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """" instantiation object method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return a dict representation """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {attr: getattr(self, attr) for attr in attrs if
                    (hasattr(self, attr))}
        return (self.__dict__)

    def reload_from_json(self, json):
        """ replace attribute in object instantce"""
        for key, value in json.items():
            setattr(self, key, value)
