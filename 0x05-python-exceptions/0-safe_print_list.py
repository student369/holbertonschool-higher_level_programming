#!/usr/bin/python3
""" safe_print_list

Python function to print the elements of a list
"""


def safe_print_list(my_list=[], x=0):
    i, p = 0, 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            p = p + 1
    except IndexError as err:
        pass
    finally:
        print()
    return (p)
