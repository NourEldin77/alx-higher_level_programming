#!/usr/bin/python3
""" load_from_json_file module """


import json


def load_from_json_file(filename):
    """  creates an Object form a 'JSON file' """
    with open(filename, "r", encoding="utf-8") as f:
        return (json.loads(f.read()))
