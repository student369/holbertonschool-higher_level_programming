#!/usr/bin/python3
"""safe_function

Python function to execute a function safely.
"""


def safe_function(fct, *args):
    import sys
    pt = 0
    rs = None
    try:
        rs = fct(*args)
    except BaseException as err:
        sys.stderr.write("Exception: {}\n".format(err))
    return (rs)
