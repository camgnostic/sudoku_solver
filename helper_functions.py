#!/usr/bin/python
import math
import itertools
import copy

# BOARD SUBCLASSES:
class CellSet(object):
    """row, column, or square in a sudoku board"""
    def __init__(self, values):
        self.values = values
        self.digits = set(range(1, len(values) + 1))

    @property
    def solved(self):
        return self.digits == set(self.values)

    def remaining(self):
        return tuple(sorted(list(self.digits - set(self.values))))

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value

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
            self.rows.append(Row(copy.copy(row)))
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

    @property
    def allsquares(self):
        return sum([row for row in self.squares], [])

    def get_square(self, *args):
        if len(args) == 1:
            sqr, sqc = args[0][0], args[0][1]
        else:
            sqr, sqc = args[0], args[1]
        return self.squares[sqr][sqc]

    def shadow(self, row, col):
        return (self.rows[row], self.cols[col],
                self.get_square(cell_to_square(row, col, self.size)))

    def unshadow(self, row, col):
        return ([r for rc, r in enumerate(self.rows) if rc != row],
                [c for cc, c in enumerate(self.cols) if cc != col],
                [s for sc, s in enumerate(self.allsquares) if sc != cell_to_allsquare_index(row, col)])
        return (self.rows[:row] + self.rows[row+1:],
                self.cols[:col] + self.cols[col+1:],
                self.allsquares[:cell_to_square_index(row, col)] + self.allsquares[cell_to_square_index(row,col) + 1])

    def get_possibilities(self, row, col):
        remaining = combine_remaining(*[cellset.remaining() for cellset in self.shadow(row, col)])
        if len(remaining) == 0:
            raise Contradiction("helpful error message")
        return remaining

    def check_solubility(self):
        unsolved = get_unsolved(self.bare_board)
        for row, col in unsolved:
            self.get_possibilities(row, col)

    def update(self, row, col, new_value):
        self.bare_board[row][col] = new_value
        self.rows[row][col] = new_value
        self.cols[col][row] = new_value
        self.get_square(cell_to_square(row, col))[cell_to_square_index(row, col)] = new_value

    def solve(self, row, col):
        if self.bare_board[row][col] != 0:
            return True
        possibilities = self.get_possibilities(row, col)
        new_value = list(possibilities)[0] if len(possibilities) == 1 else False
        if new_value:
            new_value = self.update(row, col, new_value)
        return new_value

    def solve_all_easy(self):
        for row, col in get_unsolved(self.bare_board):
            self.solve(row, col)


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

def cell_to_square_index(row, col, size=9):
    square_size = int(math.sqrt(size))
    return int(row%square_size)*square_size + int(col%square_size)

def cell_to_allsquare_index(row, col, size=9):
    square_size = int(math.sqrt(size))
    return int(row/square_size)*square_size + int(col/square_size)

def board_iterator(size):
    return itertools.product(range(size), repeat=2)

def get_unsolved(board):
    """takes a bare board and returns coordinates of all unsolved squares"""
    coords = []
    for row in range(len(board)):
        coords += [(row, col) for col in range(len(board[row])) if board[row][col] == 0]
    return coords

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
    sets = [set([x,]) for x in args if type(x) == int] + [set(x) for x in args if type(x) in (list, tuple)] + [x for x in args if type(x) == set]
    remaining = sets[0]
    for s in sets:
        remaining = remaining.intersection(s)
    return tuple(sorted(list(remaining)))
