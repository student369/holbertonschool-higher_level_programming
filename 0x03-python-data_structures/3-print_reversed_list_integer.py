#!/usr/bin/python3
"""print_reversed_list_integer

Function to print a list in reverse order
"""


def print_reversed_list_integer(my_list=[]):
    for i in range((len(my_list) - 1), -1, -1):
        print("{:d}".format(my_list[i]))
