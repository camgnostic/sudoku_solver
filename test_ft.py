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


class TestOneSquarePuzzles(unittest.TestCase):
    def get_puzzles(self, size):
        for missing in ['corner', 'edge', 'middle']:
            yield (sample_puzzles.one_square[size][missing],
                   sample_puzzles.one_square[size]['solution'])

    def test_solve_large(self):
        for puzz, soln in self.get_puzzles('large'):
            self.assertEqual(solver.solve(puzz), soln)

    def test_solve_small(self):
        for puzz, soln in self.get_puzzles('small'):
            self.assertEqual(solver.solve(puzz), soln)


if __name__ == '__main__':
    unittest.main()
