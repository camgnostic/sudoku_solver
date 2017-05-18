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
        self.size = len(board)
        self.sq_size = int(math.sqrt(self.size))
        for row in board:
            self.rows.append(Row(row))
        for col in range(len(board[0])):
            self.cols.append(Column([r[col] for r in board]))
        for sqr in range(self.sq_size):
            sq_row = []
            for sqc in range(self.sq_size):
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

    def get_square(self, *args):
        if len(args) == 1:
            sqr, sqc = args[0][0], args[0][1]
        else:
            sqr, sqc = args[0], args[1]
        return self.squares[sqr][sqc]

    def shadow(self, row, col):
        return (self.rows[row], self.cols[col],
                self.get_square(cell_to_square(row, col, self.size)))

    def get_possibilities(self, row, col):
        shadow = self.shadow(row, col)
        remaining = [x.remaining() for x in shadow]
        return combine_remaining(remaining)


# PUZZLE ARRAY -> PIECES FUNCTIONS
def get_square(board, squarerow, squarecol):
    """return the section of board corresponding to a square region"""
    size = int(math.sqrt(len(board)))
    return [row[squarecol*size:squarecol*size+size] for row in board[squarerow*size:squarerow*size+size]]

def get_square_values(square_array):
    return [x for row in square_array for x in row]

def cell_to_square(row, col, size=9):
    square_size = int(math.sqrt(size))
    return (int(row/square_size), int(col/square_size))

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

def combine_remaining(*args):
    """takes a tuple of tuples/lists/sets of digits and returns the set intersection"""
    sets = [set([x,]) for x in args if type(x) == int] + [set(x) for x in args if type(x) != int]
    remaining = sets[0]
    for s in sets:
        remaining = remaining.intersection(s)
    return tuple(sorted(list(remaining)))
