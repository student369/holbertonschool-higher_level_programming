#!/usr/bin/python3
""" Module 7-error_code

Python script that handle some http errors.
"""
import requests
import sys
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        r = requests.get(url)
        if r.status_code >= 400:
            print("Error code: {}".format(r.status_code))
        else:
            print("{}".format(r.text))
    except IndexError:
        pass
