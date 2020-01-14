#!/usr/bin/python3
""" Module 3-error_code

Python script that handle some http errors.
"""
import urllib.request
import sys
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as r:
            if r.code >= 400:
                print("Error code: {}".format(r.code))
            else:
                html = r.read()
                print("Error code: {}".format(html.decode("UTF-8")))
