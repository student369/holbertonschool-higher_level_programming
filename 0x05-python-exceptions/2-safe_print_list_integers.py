#!/usr/bin/python3
"""safe_print_list_integers

Python function to print the first x
integer elements of a list.
"""


def safe_print_list_integers(my_list=[], x=0):
    i, p = 0, 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            p = p + 1
        except (TypeError, ValueError):
            pass
    print()
    return (p)
