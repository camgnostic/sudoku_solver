#!/usr/bin/python
import itertools

def switcher(puzzle):
    """puzzle -> None (if solved) next_step_function (if not solved)"""
    if is_solved(puzzle):
        return None
    # check for one square missing, from top left to bottom right
    for r, c in board_iterator(puzzle):
        if puzzle[r].count(0) == 1:
            return solve_row(r)

def is_solved(puzzle):
    """puzzle -> True (if solved) False (if not solved)"""
    # check for a 0 in each row, if 0 found, return False
    for row in puzzle:
        if 0 in row:
            return False
    return True


def solve_row(row):
    def this_solve_row(puzzle):
        return puzzle
    return this_solve_row
        # digit = set(range(1, len(puzzle)+1)) - set(puzzle[row])
        # assert len(digit) == 1, "solve row called with multiple possibilities: " + str(puzzle[row])
        # puzzle[row][puzzle[row].index(0)] = digit.pop()
        # return puzzle

# HELPER FUNCTIONS:
def board_iterator(board):
    """ takes board, returns top left to bottom right iterator of rows/cols"""
    return itertools.product(range(len(board)), repeat=2)
