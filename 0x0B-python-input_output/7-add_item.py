#!/usr/bin/python3
""" add_item module """


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arguments = sys.argv[1:]

try:
    items_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    items_list = []

for arg in arguments:
    items_list.append(arg)

save_to_json_file(items_list, "add_item.json")
