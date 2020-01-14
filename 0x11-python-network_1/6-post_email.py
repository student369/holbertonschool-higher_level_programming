#!/usr/bin/python3
""" Module 6-post_email

Python script that get do a POST requests
with a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        data = {"email": sys.argv[2]}
        r = requests.post(url, data)
        print("{}".format(r.text))
    except IndexError:
        pass
