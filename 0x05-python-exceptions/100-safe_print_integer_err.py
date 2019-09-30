#!/usr/bin/python3
"""safe_print_integer_err

Python function to prints an integer of a list.
"""


def safe_print_integer_err(value):
    import sys
    pt = 0
    try:
        print("{:d}".format(value))
        pt = 1
    except TypeError as errt:
        sys.stderr.write("Exception: {}\n".format(errt))
    except ValueError as errv:
        sys.stderr.write("Exception: {}\n".format(errv))
    return (True if pt == 1 else False)
