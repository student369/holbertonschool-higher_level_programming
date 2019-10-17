#!/usr/bin/python3
"""Module 7-save_to_json_file
that save the JSON respeentation of an
object in a text file.
"""


def save_to_json_file(my_obj, filename):
    """ Returns Nothing

    A function that get the JSON representation
    of an object and save in a file..

    Args:
        my_obj (object): The Python object.
        filename (str): The file to store it.
    """
    if not isinstance(filename, str):
        raise TypeError("It's not a valid filename.")
    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
