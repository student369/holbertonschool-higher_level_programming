#!/usr/bin/python3
for c in range(97, 123):
    if c is not 113 and c is not 101:
        print("{:c}".format(c), end="")
