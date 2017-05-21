#!/usr/bin/python

import solver
import sample_puzzles

import unittest

class TestSolvedPuzzles(unittest.TestCase):
    def test_solve_large(self):
        self.assertEqual(sample_puzzles.solved9,
                         solver.solve(sample_puzzles.solved9))

    def test_solve_small(self):
        self.assertEqual(sample_puzzles.solved4,
                         solver.solve(sample_puzzles.solved4))

if __name__ == '__main__':
    unittest.main()
