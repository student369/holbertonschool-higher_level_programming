#!/usr/bin/python3
def remove_char_at(str, n):
    if n == 0:
        return str[n + 1:]
    if n > 0:
        if n < len(str):
            return str[:n] + str[n + 1:]
        else:
            return str
    else:
        return str
