#!/usr/bin/python3
""" Module 8-json_api

Python script that do an api request.
"""
import requests
import sys
if __name__ == "__main__":
    try:
        url = "http://0.0.0.0:5000/search_user"
        argc = len(sys.argv)
        values = {"q": ""}
        if argc >= 2:
            values = {"q": sys.argv[1]}
        r = requests.post(url, data=values)
        rjson = r.json()
        if r.headers["content-type"] is "application/json":
            print("Not a valid JSON")
        elif len(rjson) == 0:
            print("No result")
        else:
            print("[{}] {}".format(rjson.get("id"), rjson.get("name")))
    except IndexError:
        pass
