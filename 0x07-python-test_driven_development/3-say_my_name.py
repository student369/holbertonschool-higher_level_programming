#!/usr/bin/python3
""" Module 3-say_my_name

Module that contains the function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """ Returns My name is <first_name> <last_name>

    Arguments:
        first_name (str): The name
        last_name (str): The last name
    """
    fn_err = "first_name must be a string"
    ln_err = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(fn_err)
    if not isinstance(last_name, str):
        raise TypeError(ln_err)
    print("My name is {:s} {:s}"
          .format(first_name, last_name))
