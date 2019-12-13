#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 0-select_states.py

This script allow you list
all the states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Main

    A simple script to list all the states
    """
    u, p, d = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3396,
                         user=u, passwd=p, db=d)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
