#!/usr/bin/python3
"""list_division

Python function to divide the values of
two lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    l1, l2 = len(my_list_1), len(my_list_2)
    rst = 0
    rlist = []
    try:
        for i in range(list_length):
            try:
                if my_list_2[i] == 0:
                    raise ZeroDivisionError
                if isNNum(my_list_1[i]) or isNNum(my_list_2[i]):
                    raise TypeError
                rst = (my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                rst = 0
                print("division by 0")
            except TypeError:
                rst = 0
                print("wrong type")
            except IndexError:
                rst = 0
                print("out of range")
            rlist.append(rst)
    except (NotImplementedError, IndexError):
        rlist.append(0)
    finally:
        return (rlist)


def isNNum(val):
    if isinstance(val, int) or isinstance(val, float):
        return (False)
    else:
        return (True)
