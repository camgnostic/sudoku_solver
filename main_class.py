#!/usr/bin/python

from helper_functions import print_bare_board

class Board(object):
    """main class for holding a puzzle board and generating tools for solving"""

    def __init__(self, board):
        self.bare_board = board

    def __str__(self):
        return print_bare_board(self.bare_board)

    @property
    def solved(self):
        return False
