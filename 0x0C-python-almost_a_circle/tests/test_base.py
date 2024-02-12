#!/usr/bin/python3
""" TestBase Module """


import unittest
from models.base import Base


class TeatBase(unittest.TestCase):
    """Test Class for Base class
    :inherits unittest TestCase method
    """
    def test_id_attr(self):
        """ check the defualt id """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_attr_custom(self):
        """ check the id when passing a custom one """
        b3 = Base(10)
        self.assertEqual(b3.id, 10)
