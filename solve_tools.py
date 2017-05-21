#!/usr/bin/python
import itertools

def switcher(puzzle):
    """puzzle -> None (if solved) next_step_function (if not solved)"""
    if is_solved(puzzle):
        return None
    # check for rows with one digit missing:
    for r in range(len(puzzle)):
        if puzzle[r].count(0) == 1:
            return solve_row(r)
    # check for cols with one digit missing:
    for c in range(len(puzzle[0])):
        if [row[c] for row in puzzle].count(0) == 1:
            return solve_col(c)
    raise

def is_solved(puzzle):
    """puzzle -> True (if solved) False (if not solved)"""
    # check for a 0 in each row, if 0 found, return False
    for row in puzzle:
        if 0 in row:
            return False
    return True


def solve_row(row):
    def this_solve_row(puzzle):
        digit = set(range(1, len(puzzle)+1)) - set(puzzle[row])
        assert len(digit) == 1, "solve row called with multiple possibilities: " + str(puzzle[row])
        puzzle[row][puzzle[row].index(0)] = digit.pop()
        return puzzle
    return this_solve_row

def solve_col(col):
    def this_solve_col(puzzle):
        digit = set(range(1, len(puzzle[0])+1)) - set([row[col] for row in puzzle])
        assert len(digit) == 1, "solve col called with multiple possibilities: " + str([row[col] for row in puzzle])
        puzzle[[row[col] for row in puzzle].index(0)][col] = digit.pop()
        return puzzle
    return this_solve_col

# HELPER FUNCTIONS:
def board_iterator(board):
    """ takes board, returns top left to bottom right iterator of rows/cols"""
    return itertools.product(range(len(board)), repeat=2)
