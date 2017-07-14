#!/usr/bin/python3

def solve_one(group):
    group[group.index(0)] = (set(range(1, 10)) - set(group)).pop()
    return group
