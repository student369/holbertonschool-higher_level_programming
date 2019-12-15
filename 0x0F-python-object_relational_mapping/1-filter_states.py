#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 1-filter_states.py

This script allow you list
all the states that begins with N
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Main

    A simple script to list all the states
    that begins with N
    """
    u, p, d = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3396,
                         user=u, passwd=p, db=d)
    cur = db.cursor()
    let = 'N'
    cur.execute("SELECT id, name FROM states WHERE \
    states.name LIKE '{:s}%' ORDER BY states.id;".format(let))
    rows = cur.fetchall()
    for r in rows:
        if r[1][0] == let:
            print(r)
    cur.close()
    db.close()
