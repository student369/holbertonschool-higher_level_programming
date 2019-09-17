#!/usr/bin/python3
"""multiple_returns

Function to return a tuple with the lengt and first character
"""


def multiple_returns(sentence):
    new_tuple = []
    lengt = len(sentence)
    new_tuple.append(lengt)
    new_tuple.append(None if lengt is 0 else sentence[0])
    return (tuple(new_tuple))
