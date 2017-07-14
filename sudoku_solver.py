#!/usr/bin/python3

import group

def solve(puzzle):
    for row_number in range(len(puzzle)):
        puzzle[row_number] = group.solve_one(puzzle[row_number])
    return puzzle
