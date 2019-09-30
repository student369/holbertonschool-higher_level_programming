#!/usr/bin/python3
"""safe_print_integer

Python function to print an integer of a list.
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        pass
    return (False)
