#!/usr/bin/python3
""" Module 4-hbtn_status

Python script that fetch an URL
"""
import requests
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    print(
        "Body response:\n\t- type: {}\n\t- content: {}".format(
            type(r.text), r.text))
