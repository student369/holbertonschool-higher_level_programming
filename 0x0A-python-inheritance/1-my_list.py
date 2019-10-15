#!/usr/bin/python3
""" Module 7-rectangle

Module that contains the class MyList
"""


class MyList(list):
    """ Rectangle class

    A empty MyList class.
    """

    def print_sorted(self):
        """Returns nothing

        This function prints the list in
        order.
        """
        print(sorted(self))

    def append(self, i):
        """Returns None

        Added a validation in case of a not number
        """
        if not isinstance(i, int):
            raise TypeError("Must be an integers list.")
        super(MyList, self).append(i)
