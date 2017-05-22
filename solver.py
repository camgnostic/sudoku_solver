#!/usr/bin/python
import solve_tools

def solve(puzzle):
    puzzle, solved = solve_tools.solve_single_possibilities(puzzle)
    if solved:
        return puzzle
    else:
        raise
