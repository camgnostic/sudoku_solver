#!/usr/bin/python

import unittest
import solve_tools
import sample_puzzles


class TestIsSolved(unittest.TestCase):
    """ True if solved else False"""
    def test_solved_puzzle(self):
        assert solve_tools.is_solved(sample_puzzles.solved4)
        assert solve_tools.is_solved(sample_puzzles.solved9)

    def test_unsolved_puzzle(self):
        assert not solve_tools.is_solved(sample_puzzles.one_square['large']['edge'])
        assert not solve_tools.is_solved(sample_puzzles.one_square['small']['corner'])


class TestGetNextStep(unittest.TestCase):
    """ chooses the next action based on the puzzle:

        cases:
            1. puzzle is solved (return None)
            2. puzzle has 1 unsolved spot (return find_single_spot)
    """
    def test_solved_puzzle(self):
        switcher = solve_tools.switcher
        self.assertEqual(switcher(sample_puzzles.solved4), None)
        self.assertEqual(switcher(sample_puzzles.solved9), None)

    def test_one_unsolved_in_row(self):
        # for the first row:
        puzzle = [[1, 2, 3, 4, 5, 0, 7, 8, 9],] + [[0]*9]*8
        self.assertEqual(solve_tools.switcher(puzzle).__name__,
                         solve_tools.solve_row(0).__name__)
        # and for a row in the middle:
        puzzle = [[0]*9]*3 + [[1, 2, 3, 4, 5, 0, 7, 8, 9],] + [[0]*9]*5
        self.assertEqual(solve_tools.switcher(puzzle).__name__,
                         solve_tools.solve_row(3).__name__)

class TestSolveRow(unittest.TestCase):
    def test_solve_row0(self):
        solve_row = solve_tools.solve_row(0)
        puzzle = [[1, 2, 3, 4, 5, 0, 7, 8, 9],] + [[0]*9]*8
        self.assertEqual(solve_row(puzzle)[0], [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()
