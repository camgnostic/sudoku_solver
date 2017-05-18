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


# PRINTING/FORMATTING:
def print_bare_board(board):
    pretty = ''
    for row in board:
        for cell in row[:-1]:
            pretty += ' %d |' % cell
        pretty += ' %d \n' % row[-1]
    return pretty.replace('0', ' ')[:-1]

