#!/usr/bin/python
import itertools
import math

from helper_functions import (print_bare_board,
                              Contradiction,
                              SubBoard,
                              Row,
                              Column,
                              Square,
                              get_square)

class Board(object):
    """main class for holding a puzzle board and generating tools for solving"""

    def __init__(self, board):
        self.board = SubBoard(board)

    def __str__(self):
        return print_bare_board(self.board.bare_board)

    @property
    def solved(self):
        return (all([row.solved for row in self.board.rows]) and
                all([col.solved for col in self.board.cols]) and
                all([square.solved for square in self.board.allsquares]))

    @property
    def solution(self):
        if self.solved:
            return self.board.bare_board
        return False

    @property
    def soluble(self):
        try:
            self.board.check_solubility()
        except Contradiction:
            return False
        else:
            return True

    def solve_easy(self):
        self.board.solve_all_easy()
        return self.solved
