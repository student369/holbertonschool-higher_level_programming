#!/usr/bin/python3
""" Module 1-hbtn_header

Python script that get the X-Request-Id header
from the response.
"""
import urllib.request
import sys
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as r:
            print(r.headers["X-Request-Id"])
    except IndexError:
        pass
