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
    """takes column number, old puzzle, and a list of 9 to put in that column, returns updated puzzle"""
    for rowno in range(len(puzzle)):
        puzzle[rowno][colno] = newcolumn[rowno]
    return puzzle


def get_square(squareno, puzzle):
    """takes square number (left to right then top to bottom) returns a list of 9 numbers"""
    return puzzle[squareno][0:3] + puzzle[squareno+1][0:3] + puzzle[squareno+2][0:3]
