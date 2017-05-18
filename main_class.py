#!/usr/bin/python
import itertools

from helper_functions import (print_bare_board,
                              Row,
                              Column,
                              Square,
                              get_square)

class Board(object):
    """main class for holding a puzzle board and generating tools for solving"""
    rows = []
    cols = []
    squares = []

    def __init__(self, board):
        self.bare_board = board
        for row in board:
            self.rows.append(Row(row))
        for col in range(len(board[0])):
            self.cols.append(Column([r[col] for r in board]))
        for sqr, sqc in itertools.product([0, 1, 2], repeat=2):
            self.squares.append(Square(get_square(board, sqr, sqc)))

    def __str__(self):
        return print_bare_board(self.bare_board)

    @property
    def solved(self):
        return (all([row.solved for row in self.rows]) and
                all([col.solved for col in self.cols]) and
                all([square.solved for square in self.squares]))
