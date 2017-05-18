#!/usr/bin/python

# BOARD SUBCLASSES:
class CellSet(object):
    """row, column, or square in a sudoku board"""
    def __init__(self, values):
        self.values = values

    @property
    def solved(self):
        digits = set(range(1, 10))
        return digits == set(self.values)

class Row(CellSet):
    """one row in a sudoku board"""
    pass

class Column(CellSet):
    """one column in a sudoku board"""
    pass

class Square(CellSet):
    """one square region in a sudoku board"""
    def __init__(self, rows):
        self.rows = rows
        self.values = get_square_values(rows)


# PUZZLE ARRAY -> PIECES FUNCTIONS
def get_square(board, squarerow, squarecol):
    """return the section of board corresponding to a square region"""
    return [row[squarecol*3:squarecol*3+3] for row in board[squarerow*3:squarerow*3+3]]

def get_square_values(square_array):
    return [x for row in square_array for x in row]

# PRINTING/FORMATTING:
def print_bare_board(board):
    pretty = ''
    for row in board:
        for cell in row[:-1]:
            pretty += ' %d |' % cell
        pretty += ' %d \n' % row[-1]
    return pretty.replace('0', ' ')[:-1]

