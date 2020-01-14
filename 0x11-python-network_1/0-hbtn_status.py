#!/usr/bin/python3
""" Module 0-hbtn_status

Python script that fetch an URL
"""
import urllib.request
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as r:
        html = r.read()
        print(
            """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(
                type(html), html, html.decode("UTF-8")
            )
        )
        """
        print("- type: {}".format(type(html)))
        print("- content: {}".format(html))
        print("- utf8 content: {:s}".format(html.decode("UTF-8")))
        """
