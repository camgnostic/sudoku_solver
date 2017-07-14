#!/usr/bin/python3

import unittest
import group

#puzzle_structure = [[x]*9 for x in range(1,10)]


class TestIsDiscovered(unittest.TestCase):
    def test_row_is_solved(self):
        assert group.solve_one([0] + list(range(2, 10))) == list(range(1, 10))

    def test_row_with_random_missing_is_solved(self):
        row = [4, 1, 2, 3, 6, 5, 8, 9, 7]
        assert group.solve_one(row[:4] + [0] + row[5:]) == row

    def test_row_with_no_missing_is_returned(self):
        assert group.solve_one(list(range(1, 10))) == list(range(1, 10))
