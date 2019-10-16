#!/usr/bin/python3
""" Module 4-append_write

Module that contains the function to_json_string
that return a JSON from an object.
"""


def to_json_string(my_obj):
    """ Returns a representation in JSON of an object

    A function that get the JSON representation
    of an object.

    Args:
        my_obj (object): The Python object
    """
    import json
    return (json.dumps(my_obj))
