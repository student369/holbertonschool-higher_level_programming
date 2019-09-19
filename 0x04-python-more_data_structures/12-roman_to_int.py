#!/usr/bin/python3
"""roman_to_int

Function to convert a Roman number to integer.
"""


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)
    rom = {"I": 1, "V": 5, "X": 10, "L": 50,
           "C": 100, "D": 500, "M": 1000}
    strg = roman_string
    els = len(strg)
    if els == 0:
        return (None)
    sum = 0
    if els == 1:
        sum = rom[strg[0]]
    else:
        for i in range(1, els):
            if strg[i] == "M" and strg[i - 1] == "C":
                sum = sum - rom["C"]
            if strg[i] == "C" and strg[i - 1] == "X":
                sum = sum - rom["X"]
            if strg[i] == "X" and strg[i - 1] == "I":
                sum = sum - rom["I"]
            if rom[strg[i - 1]] < rom[strg[i]]:
                sum = sum + (rom[strg[i]] - rom[strg[i - 1]])
            else:
                if i == 1:
                    sum = sum + (rom[strg[i]] + rom[strg[i - 1]])
                else:
                    sum = sum + (rom[strg[i]])
    return (sum)
