#!/usr/bin/python
import itertools
import math
import copy

def solve_single_possibilities(puzzle):
    while True:
        next_steps_gen = singles_switcher(puzzle)
        for next_step in next_steps_gen:
            if next_step is None:
                return puzzle, True
            elif next_step is True:
                raise NotImplementedError("Should never see True here")
            elif next_step is False:
                return puzzle, False
            else:
                puzzle = next_step(puzzle)
    raise NotImplementedError("should return before loop finishes")

def solve_single_spot(puzzle):
    pass
    

def singles_switcher(puzzle):
    """puzzle -> None (if solved) next_step_function (if not solved and single possibility)"""
    if is_solved(puzzle):
        yield None
    restart = False
    # check for rows with one digit missing:
    for r in range(len(puzzle)):
        if puzzle[r].count(0) == 1:
            restart = True
            yield solve_row(r)
    if restart: # we've changed something, start over before doing cols
        return
    for c in range(len(puzzle[0])):
        if [row[c] for row in puzzle].count(0) == 1:
            restart = True
            yield solve_col(c)
    if restart: # we've changed something, start over before doing cols
        return
    for r, c in square_iterator(puzzle):
        if get_square_flat(r, c)(puzzle).count(0) == 1:
            restart = True
            yield solve_square(r, c)
    if not restart:
        yield False
    return

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
        r, c = get_square_index(puzzle)(sqr, sqc)(square_flattener(puzzle).index(0))
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

def get_column_values(puzzle, col):
    return [row[col] for row in puzzle]

def get_possibility_fn(cell_set):
    digits = set(range(1, len(cell_set)+1)) - set([cell for cell in cell_set if type(cell) != tuple])
    def poss_fn(cell):
        if type(cell) == tuple:
            return tuple(sorted(list(set(cell).intersection(digits))))
        elif type(cell) == int:
            if cell == 0:
                return tuple(sorted(list(digits)))
            else:
                return cell
        else:
            raise
    return poss_fn

def get_possibility_map(bare_puzzle):
    puzzle = copy.deepcopy(bare_puzzle)
    row_fns = [get_possibility_fn(row) for row in puzzle]
    col_fns = [get_possibility_fn(get_column_values(puzzle, col)) for col in range(len(puzzle[0]))]
    sq_fns = {rctuple: get_possibility_fn(get_square_flat(*rctuple)(puzzle)) for rctuple in square_iterator(puzzle)}
    step = int(math.sqrt(len(puzzle)))
    for r, c in board_iterator(puzzle):
        puzzle[r][c] = sq_fns[(int(r/step)*step, int(c/step)*step)](col_fns[c](row_fns[r](puzzle[r][c])))
    return puzzle

def unmap(poss_map):
    return [map(lambda cell: cell if type(cell) != tuple else 0, row) for row in poss_map]


