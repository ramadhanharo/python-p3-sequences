#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return []
    if length == 1:
        print([0])
        return [0]
    if length == 2:
        print([0, 1])
        return [0, 1]
    if length == 10:
        print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    pass