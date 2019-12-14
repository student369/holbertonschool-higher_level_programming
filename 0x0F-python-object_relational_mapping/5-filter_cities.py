#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module 5-filter_cities.py

This script allow you list
all the cities of an state
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Main

    A simple script to list all the cities
    of an state
    """
    u, p, d = sys.argv[1], sys.argv[2], sys.argv[3]
    sname = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3396,
                         user=u, passwd=p, db=d)
    cur = db.cursor()
    sql = "SELECT c.name \
FROM cities AS c INNER JOIN states AS s \
    ON c.state_id = s.id AND s.name = %(sname)s;"
    cur.execute(sql, {"sname": sname})
    rows = cur.fetchall()
    result = ""
    for r in rows:
        for c in r:
            result += "{:s}, ".format(c)
    print(result[0:-2])
    cur.close()
    db.close()
