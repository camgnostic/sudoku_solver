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

    def test_one_unsolved_spot(self):
        switcher = solve_tools.switcher
        one_spot = solve_tools.find_single_spot
        self.assertIsNotNone(switcher(sample_puzzles.one_square['large']['corner']))
        self.assertEqual(switcher(sample_puzzles.one_square['large']['corner']),
                         one_spot(1,8))
        self.assertEqual(switcher(sample_puzzles.one_square['small']['edge']),
                         one_spot(3, 1))

if __name__ == '__main__':
    unittest.main()
