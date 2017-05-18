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
    def test_row_exists(self):
        row = hf.Row(unsolved_row)
        


if __name__ == '__main__':
    unittest.main()
