#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print("{}".format(n))
    else:
        print("{}, ".format("0" + str(n) if n < 10 else str(n)), end="")
