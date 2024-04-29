#!/usr/bin/python3
"""List all states starting with a from hbtn_03_0_usa"""

import MySQLdb
import sys

if len(sys.argv) > 1:
    arg = sys.argv
    connection = MySQLdb.connect(host="localhost", user=arg[1],
                                 password=arg[2],
                                 database=arg[3],
                                 port=3306)
    cursor = connection.cursor()
    q = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(arg[4])
    cursor.execute(q)
    states = cursor.fetchall()
    for row in states:
        print(row)
