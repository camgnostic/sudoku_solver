#!/usr/bin/python

import helper_functions as hf
import sample_puzzles as puzzles
import unittest

class TestPrintingFunctions(unittest.TestCase):
    def test_pretty_print_bare_board(self):
        puzzle = puzzles.medium_puzzle
        pretty = puzzles.pretty_medium_puzzle
        assert hf.print_bare_board(puzzle) == pretty, \
            '%s\n != \n%s' % (repr(pretty), repr(hf.print_bare_board(puzzle)))

class TestRowFunctions(unittest.TestCase):
    unsolved_row = puzzles.medium_puzzle[0]
    solved_row = puzzles.medium_solution[0]

    def test_row_exists(self):
        row = hf.Row(self.unsolved_row)

    def test_row_identifies_unsolved(self):
        row = hf.Row(self.unsolved_row)
        assert not row.solved

    def test_row_identifies_solved(self):
        row = hf.Row(self.solved_row)
        assert row.solved

class TestColumnFunctions(unittest.TestCase):
    unsolved_column = [row[0] for row in puzzles.medium_puzzle]
    solved_column = [row[0] for row in puzzles.medium_solution]

    def test_column_exists(self):
        column = hf.Column(self.unsolved_column)

    def test_column_identifies_unsolved(self):
        column = hf.Column(self.unsolved_column)
        assert not column.solved

    def test_column_identifies_solved(self):
        column = hf.Column(self.solved_column)
        assert column.solved

class TestSquareFunctions(unittest.TestCase):
    whole_puzzle = puzzles.medium_puzzle
    square_0_2 = [[0,0,0], [0,0,0], [0,6,0]]
    square_1_1 = [[0,6,0], [8,0,3], [0,2,0]]
    def test_square_values_identified(self):
        assert hf.get_square(self.whole_puzzle, 1, 1) == self.square_1_1, \
            '%s != %s' % (str(hf.get_square(self.whole_puzzle, 1, 1)), str(self.square_1_1))
        assert hf.get_square(self.whole_puzzle, 0, 2) == self.square_0_2, \
            '%s != %s' % (str(hf.get_square(self.whole_puzzle, 0, 2)), str(self.square_0_2))


if __name__ == '__main__':
    unittest.main()
