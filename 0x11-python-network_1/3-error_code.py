#!/usr/bin/python3
""" Module 3-error_code

Python script that handle some http errors.
"""
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        url = sys.argv[1]
        with urllib.request.urlopen(url) as r:
            html = r.read()
            print(html.decode("UTF-8"))
    except IndexError:
        pass
    except urllib.error.URLError as e:
        if e.code >= 400:
            print("Error code: {}".format(e.code))
