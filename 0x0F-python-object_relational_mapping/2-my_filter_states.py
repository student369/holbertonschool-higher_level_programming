#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 2-my_filter_states.py

This script allow you list
all the states that begins
with the given name
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Main

    A simple script to list all the states
    that begins with the given name
    """
    u, p, d = sys.argv[1], sys.argv[2], sys.argv[3]
    name = sys.argv[4]
    name = str(name).replace("'", "")
    name = str(name).replace('"', "")
    db = MySQLdb.connect(host="localhost", port=3396,
                         user=u, passwd=p, db=d)
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE states.name = \
'{:s}' ORDER BY states.id;".format(name)
    cur.execute(sql)
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
