#!/usr/bin/python3
""" form_json_string module """


import json


def from_json_string(my_str):
    """ return an object represented by JSON string"""
    return (json.loads(my_str))
