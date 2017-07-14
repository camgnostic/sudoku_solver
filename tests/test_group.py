#!/usr/bin/python3

import unittest
import group

#puzzle_structure = [[x]*9 for x in range(1,10)]


class TestIsDiscovered(unittest.TestCase):
    def test_row_is_solved(self):
        assert group.solve_one([0] + list(range(2, 10))) == list(range(1, 10))
