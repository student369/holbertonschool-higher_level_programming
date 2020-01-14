#!/usr/bin/python3
""" Module 5-hbtn_header.py

Python script that get a X-Request-Id header
"""
import requests
import sys
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        r = requests.get(url)
        h = r.headers["X-Request-Id"]
        print("{}".format(h))
    except IndexError:
        pass
