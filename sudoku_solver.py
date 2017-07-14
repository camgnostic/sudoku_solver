#!/usr/bin/python3

import group

def solve(puzzle):
    for row_number in range(len(puzzle)):
        puzzle[row_number] = group.solve_one(puzzle[row_number])
    for col_number in range(len(puzzle)):
        group.set_column(col_number, puzzle,
                         group.solve_one(group.get_column(col_number, puzzle)))
    for square_number in range(len(puzzle)):
        group.set_square(square_number, puzzle,
                         group.solve_one(group.get_square(square_number, puzzle)))
    return puzzle
