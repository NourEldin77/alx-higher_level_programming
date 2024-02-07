#!/usr/bin/python3
""" save_to_json_file module """


import json


def save_to_json_file(my_obj, filename):
    """" wirtes an Object to text file using JSON """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
