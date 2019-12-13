#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 3-my_save_filter_states.py

This script allow you list
all the states that begins
with the given name securely
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Main

    A simple script to list all the states
    that begins with the given name
    securely
    """
    u, p, d = sys.argv[1], sys.argv[2], sys.argv[3]
    name = sys.argv[4]
    """
    name = str(name).replace("'", "")
    name = str(name).replace('"', "")
    """
    db = MySQLdb.connect(host="localhost", port=3396,
                         user=u, passwd=p, db=d)
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE states.name = \
%(name)s ORDER BY states.id;"
    cur.execute(sql, {"name": name})
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
