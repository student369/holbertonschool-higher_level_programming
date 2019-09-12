#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac, av = len(sys.argv), sys.argv
    if ac < 2:
        print("{:d} arguments.".format(0))
    elif ac == 2:
        print("{:d} argument:".format(1))
        print("{:d}: {:s}".format(1, av[1]))
    else:
        print("{:d}: arguments:".format(ac - 1))
        for i in range(ac):
            if i != 0:
                print("{:d}: {:s}".format(i, av[i]))
