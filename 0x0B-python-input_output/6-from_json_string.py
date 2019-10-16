#!/usr/bin/python3
""" Module 6-from_json_string

Module that contains the function from_json_string
that return a JSON from an object.
"""


def from_json_string(my_str):
    """Returns an object from a JSON string.

    A function that get the Python object
    from the JSON string.

    Args:
        my_str (str): The JSON string.
    """
    import json
    return (json.loads(my_str))
