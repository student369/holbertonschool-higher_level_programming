#!/usr/bin/python3
""" Module 8-load_from_json_file

Module that contains the function load_from_json_file
that return a Python object from a JSON sting file.
"""


def load_from_json_file(filename):
    """Returns an object from a JSON string.

    A function that get the Python object
    from the JSON string in an textfile.

    Args:
        filename (str): The JSON filename file..
    """
    if not isinstance(filename, str):
        raise TypeError("It's not a valid filename.")
    import json
    with open(filename, mode="r", encoding="utf-8") as f:
        return (json.loads(f.read()))
