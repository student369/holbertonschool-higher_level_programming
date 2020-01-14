#!/usr/bin/python3
""" Module 9-startwars

Python script that do an api request.
"""
import requests
import sys
if __name__ == "__main__":
    args = sys.argv[1]
    url = "https://swapi.co/api/people/?search={}".format(args)
    r = requests.get(url)
    r = r.json()
    print("Number of results: {}".format(r.get("count")))
    for n in r.get("results"):
        print(n["name"])
