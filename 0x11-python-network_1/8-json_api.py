#!/usr/bin/python3
""" Module 8-json_api

Python script that do an api request.
"""
import requests
import sys
if __name__ == "__main__":
    try:
        url = "http://0.0.0.0:5000/search_user"
        if sys.argc < 2:
            data = {"q": ""}
        else:
            data = {"q": sys.argv[1]}
        r = requests.post(url, data)
        try:
            if r.json == "":
                print("No result")
                exit()
            if json.loads(r.json):
                dic = json.loads(r.json)
                print("[{}] {}".format(
                    dic["id"], dic["name"]))
        except ValueError:
            print("Not a valid JSON")
            exit()
    except IndexError:
        pass
