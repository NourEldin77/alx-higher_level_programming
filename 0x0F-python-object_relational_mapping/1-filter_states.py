#!/usr/bin/python3
"""List all states starting with a from hbtn_03_0_usa"""

import MySQLdb
import sys

if len(sys.argv) > 1:
    arguments = sys.argv
    connection = MySQLdb.connect(host="localhost", user=arguments[1],
                                 password=arguments[2],
                                 database=arguments[3],
                                 port=3306)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    states = cursor.fetchall()
    for row in states:
        if row[1][0] == 'N':
            print(row)
