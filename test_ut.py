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

    def test_one_unsolved_in_col(self):
        # for the first col:
        puzzle = []
        for x in range(9):
            puzzle.append([x,] + [0]*8)
        self.assertEqual(solve_tools.switcher(puzzle).__name__,
                         solve_tools.solve_col(0).__name__)
        # and for a col in the middle:
        puzzle = []
        for x in range(9):
            puzzle.append([0]*4 + [x,] + [0]*4)
        self.assertEqual(solve_tools.switcher(puzzle).__name__,
                         solve_tools.solve_col(4).__name__)

    def test_one_unsolved_in_square(self):
        # for the first square:
        puzzle = [
            [1, 2, 3] + [0]*6,
            [4, 5, 6] + [0]*6,
            [7, 0, 9] + [0]*6
        ] + [[0]*9]*6
        self.assertEqual(solve_tools.switcher(puzzle).__name__,
                         solve_tools.solve_square(0, 0).__name__)
        # and for a square in the middle:
        puzzle = [[0]*9]*3 + [
            [0]*3 + [1, 2, 3] + [0]*3,
            [0]*3 + [4, 5, 6] + [0]*3,
            [0]*3 + [7, 0, 9] + [0]*3
        ] + [[0]*9]*3
        self.assertEqual(solve_tools.switcher(puzzle).__name__,
                         solve_tools.solve_square(3, 3).__name__)

class TestSolveRowAndColAndSquare(unittest.TestCase):
    def test_solve_row0(self):
        solve_row = solve_tools.solve_row(0)
        puzzle = [[1, 2, 3, 4, 5, 0, 7, 8, 9],] + [[0]*9]*8
        self.assertEqual(solve_row(puzzle)[0], [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_solve_row6(self):
        solve_row = solve_tools.solve_row(6)
        puzzle = [[0]*9]*6 + [[1, 2, 3, 4, 5, 0, 7, 8, 9],] + [[0]*9]*2
        self.assertEqual(solve_row(puzzle)[6], [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_solve_col0(self):
        solve_col = solve_tools.solve_col(0)
        puzzle = []
        for x in range(9):
            puzzle.append([x,] + [0]*8)
        self.assertEqual(solve_col(puzzle)[0][0], 9)

    def test_solve_col5(self):
        solve_col = solve_tools.solve_col(5)
        puzzle = []
        for x in range(9):
            puzzle.append([0]*5 + [x,] + [0]*3)
        self.assertEqual(solve_col(puzzle)[0][5], 9)

    def test_solve_square00(self):
        puzzle = [
            [1, 2, 3] + [0]*6,
            [4, 5, 6] + [0]*6,
            [7, 0, 9] + [0]*6
        ] + [[0]*9]*6
        solve_sq = solve_tools.solve_square(0, 0)
        self.assertEqual(solve_sq(puzzle)[2][1], 8)
    
    def test_solve_square33(self):
        puzzle = [[0]*9]*3 + [
            [0]*3 + [1, 2, 3] + [0]*3,
            [0]*3 + [4, 5, 6] + [0]*3,
            [0]*3 + [7, 0, 9] + [0]*3
        ] + [[0]*9]*3
        solve_sq = solve_tools.solve_square(3, 3)
        self.assertEqual(solve_sq(puzzle)[5][4], 8)

class TestSquareHelpers(unittest.TestCase):
    large_puzzle = [[0]*9]*9
    large_iterator = [(0,0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    small_puzzle = [[0]*4]*4
    small_iterator = [(0,0), (0, 2), (2, 0), (2, 2)]

    def test_large_puzzle_iterator(self):
        self.assertEqual(list(solve_tools.square_iterator(self.large_puzzle)),
                         self.large_iterator)

    def test_small_puzzle_iterator(self):
        self.assertEqual(list(solve_tools.square_iterator(self.small_puzzle)),
                         self.small_iterator)
    
    def test_get_square_flat(self):
        puzzle = [range(1, 10)]*9
        self.assertEqual(solve_tools.get_square_flat(0, 0)(puzzle),
                         [1, 2, 3, 1, 2, 3, 1, 2, 3])
        puzzle = sample_puzzles.solved9
        self.assertEqual(solve_tools.get_square_flat(6, 3)(puzzle),
                         [1, 3, 8, 7, 9, 5, 6, 4, 2])
        puzzle = sample_puzzles.solved4
        self.assertEqual(solve_tools.get_square_flat(2, 0)(puzzle),
                         [1, 3, 2, 4])

    def test_get_square_index(self):
        puzzle = [range(1, 10)]*9
        indexer = solve_tools.get_square_index(puzzle)
        self.assertEqual(indexer(0, 0)(3), (1, 0))
        self.assertEqual(indexer(0, 0)(8), (2, 2))
        self.assertEqual(indexer(6, 3)(1), (6, 4))
        self.assertEqual(indexer(6, 3)(7), (8, 4))

if __name__ == '__main__':
    unittest.main()
