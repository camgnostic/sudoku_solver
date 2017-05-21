#!/usr/bin/python
import itertools
import math

def solve_single_possibilities(puzzle):
    next_step = switcher(puzzle)
    if not next_step:
        return puzzle
    else:
        return next_step(puzzle)

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
    for r, c in square_iterator(puzzle):
        if get_square_flat(r, c)(puzzle).count(0) == 1:
            return solve_square(r, c)
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

def solve_square(sqr, sqc):
    square_flattener = get_square_flat(sqr, sqc)
    def this_solve_square(puzzle):
        digit = set(range(1, len(puzzle)+1)) - set(square_flattener(puzzle))
        assert len(digit) == 1, "solve square called with multiple possibilities: " + str(square_flattener(puzzle))
        indexer = get_square_index(puzzle)
        r, c = indexer(sqr, sqc)(square_flattener(puzzle).index(0))
        puzzle[r][c] = digit.pop()
        return puzzle
    return this_solve_square

# HELPER FUNCTIONS:
def board_iterator(board):
    """ takes board, returns top left to bottom right iterator of rows/cols"""
    return itertools.product(range(len(board)), repeat=2)

def square_iterator(board):
    """ takes board, returns top left of each square in board"""
    step = int(math.sqrt(len(board)))
    return itertools.product(range(0, len(board), step), repeat=2)

def get_square_flat(sqr, sqc):
    """coordinates of top left cell in square, returns function to return that square's values as list"""
    def square_flattener(board):
        step = int(math.sqrt(len(board)))
        return [cell for row in board[sqr:sqr+step] for cell in row[sqc:sqc+step]]
    return square_flattener

def get_square_index(puzzle):
    """ returns indexer that converts placement in a list of square values to board row and col"""
    step = int(math.sqrt(len(puzzle)))
    def indexer(sqr, sqc):
        def this_square_index(index):
            return (sqr+int(index/step), sqc + index%step)
        return this_square_index
    return indexer

