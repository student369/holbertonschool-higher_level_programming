#!/usr/bin/python3
""" Module 10-my_github

Python script that get the id of the github account.
"""
import requests
import sys
if __name__ == "__main__":
    user, psw = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(user, psw))
    rjson = r.json()
    print(rjson.get("id"))
