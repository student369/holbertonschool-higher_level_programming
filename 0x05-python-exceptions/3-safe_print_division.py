#!/usr/bin/python3
"""safe_print_division

Python function to divide two numbers
and show the result.
"""


def safe_print_division(a, b):
    rst = 0
    try:
        rst = (a / b)
    except ZeroDivisionError:
        rst = None
    finally:
        print("Inside result: {}".format(rst))
        return (rst)
