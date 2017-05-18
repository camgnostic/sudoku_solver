#!/usr/bin/python

import main_class as mc
import unittest
import sample_puzzles as puzzles

class TestBoardClass(unittest.TestCase):
    def test_class_exists(self):
        board = mc.Board
        
    def test_board_loads_puzzle(self):
        board = mc.Board(puzzles.simple_puzzle)

    def test_board_prints_output_prettily(self):
        pretty_board = puzzles.pretty_medium_puzzle
        board = mc.Board(puzzles.medium_puzzle)
        assert pretty_board == str(board), \
            '%s \n should look like: %s' % (pretty_board, str(board))

    def test_board_identifies_solved_puzzle(self):
        solved_board = mc.Board(puzzles.medium_solution)
        assert solved_board.solved

    def test_board_identifies_unsolved_puzzle(self):
        unsolved_board = mc.Board(puzzles.medium_puzzle)
        assert not unsolved_board.solved

    def test_board_loads_tiny_puzzle(self):
        board = mc.Board(puzzles.tiny_puzzle)

    def test_board_identifies_solved_tiny_puzzle(self):
        solved_board = mc.Board(puzzles.tiny_solution)
        unsolved_board = mc.Board(puzzles.tiny_puzzle)
        assert solved_board.solved
        assert not unsolved_board.solved

    def test_board_identifies_insoluble_for_no_possibilities_tiny_puzzle(self):
        insoluble_board = mc.Board(puzzles.tiny_insoluble)
        assert not insoluble_board.soluble

    def test_board_solves_single_possibility_spots(self):
        soluble_board = mc.Board(puzzles.simple_puzzle)
        assert soluble_board.solve_easy()
        assert soluble_board.solved
        assert soluble_board.solution == puzzles.simple_solution


if __name__ == '__main__':
    unittest.main()
