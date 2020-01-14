#!/usr/bin/python3
""" Module 2-post_email

Python script that send a POST request
"""
import urllib.request
import sys
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        email = sys.argv[2]
        values = {"email": email}
        data = urllib.parse.urlencode(values)
        data = data.encode("ascii")
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as r:
            html = r.read()
            print("{}".format(html.decode("UTF-8")))
    except IndexError:
        pass
