#!/usr/bin/python3
""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file after each line
    containing a specific string """
    with open(filename, "r", encoding="utf-8") as f:
        all_lines = f.readlines()
    line_num = 0
    while line_num < len(all_lines):
        if search_string in all_lines[line_num]:
            all_lines.insert(line_num + 1, new_string)
            line_num += 1
        line_num += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(all_lines)
