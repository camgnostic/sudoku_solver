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
        


if __name__ == '__main__':
    unittest.main()
