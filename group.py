#!/usr/bin/python3


def solve_one(group):
    """takes a list of 9 numbers with 1 zero, returns a list of 9 unique numbers with no zero"""
    if group.count(0) == 1:
        group[group.index(0)] = (set(range(1, 10)) - set(group)).pop()
    return group


def get_column(colno, puzzle):
    """takes a column number and a puzzle (list of lists) returns a list of values in that column"""
    return [row[colno] for row in puzzle]


def set_column(colno, puzzle, newcolumn):
    for rowno in range(len(puzzle)):
        puzzle[rowno][colno] = newcolumn[rowno]
    return puzzle
