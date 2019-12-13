#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 4-cities_by_state.py

This script allow you list
all the cities
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Main

    A simple script to list all the cities
    """
    u, p, d = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3396,
                         user=u, passwd=p, db=d)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
FROM cities AS c INNER JOIN states AS s \
    ON c.state_id = s.id ORDER BY c.id, c.name;")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
