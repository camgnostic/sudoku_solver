#!/usr/bin/python
import math
import itertools

# BOARD SUBCLASSES:
class CellSet(object):
    """row, column, or square in a sudoku board"""
    def __init__(self, values):
        self.values = values
        self.digits = set(range(1, len(values) + 1))

    @property
    def solved(self):
        return self.digits == set(self.values)

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
        values = get_square_values(rows)
        super(Square, self).__init__(values)

class SubBoard(object):
    """coordinates rows, columns, squares in a sudoku board"""
    def __init__(self, board):
        self.rows = []
        self.cols = []
        self.squares = []
        self.bare_board = board
        size = int(math.sqrt(len(board)))
        for row in board:
            self.rows.append(Row(row))
        for col in range(len(board[0])):
            self.cols.append(Column([r[col] for r in board]))
        for sqr in range(size):
            sq_row = []
            for sqc in range(size):
                sq_row.append(Square(get_square(board, sqr, sqc)))
            self.squares.append(sq_row)

    @property
    def row(self):
        return self.rows

    @property
    def col(self):
        return self.cols

    @property
    def square(self):
        return self.squares


# PUZZLE ARRAY -> PIECES FUNCTIONS
def get_square(board, squarerow, squarecol):
    """return the section of board corresponding to a square region"""
    size = int(math.sqrt(len(board)))
    return [row[squarecol*size:squarecol*size+size] for row in board[squarerow*size:squarerow*size+size]]

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

# OTHER HELPERS
class Contradiction(Exception):
    pass
