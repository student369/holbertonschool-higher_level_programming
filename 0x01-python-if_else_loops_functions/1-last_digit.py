#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
inis = "Last digit of "
if last > 5:
    ends = "is greater than 5"
    print("{}{} is {} and {}".format(inis, number, last, ends))
if last == 0:
    ends = "is 0"
    print("{}{} is {} and {}".format(inis, number, last, ends))
if last < 6 and last != 0:
    ends = "is less that 6 and not 0"
    print("{}{} is {} and {}".format(inis, number, last, ends))
