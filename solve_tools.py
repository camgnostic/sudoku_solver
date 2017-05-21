#!/usr/bin/python

def switcher(puzzle):
    """puzzle -> None (if solved) next_step_function (if not solved)"""
    if is_solved(puzzle):
        return None
    else:
        return False

def is_solved(puzzle):
    """puzzle -> True (if solved) False (if not solved)"""
    # check for a 0 in each row, if 0 found, return False
    for row in puzzle:
        if 0 in row:
            return False
    return True

def find_single_spot(row, col):
    pass
