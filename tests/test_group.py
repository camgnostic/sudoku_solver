#!/usr/bin/python3

import unittest
import group

#puzzle_structure = [[x]*9 for x in range(1,10)]


class TestSimpleListTools(unittest.TestCase):
    def test_row_is_solved(self):
        assert group.solve_one([0] + list(range(2, 10))) == list(range(1, 10))

    def test_row_with_random_missing_is_solved(self):
        row = [4, 1, 2, 3, 6, 5, 8, 9, 7]
        assert group.solve_one(row[:4] + [0] + row[5:]) == row

    def test_row_with_no_missing_is_returned(self):
        assert group.solve_one(list(range(1, 10))) == list(range(1, 10))

column_test = [[1]*3 + [x] + [1]*5 for x in range(1, 10)]


class TestColumnGetter(unittest.TestCase):
    def test_correct_column_is_returned(self):
        assert group.get_column(3, column_test) == list(range(1, 10))


class TestColumnSetter(unittest.TestCase):
    def test_column_correctly_updates(self):
        assert group.get_column(
            3, group.set_column(3, column_test, list(reversed(list(range(1, 10)))))
            ) == list(reversed(list(range(1, 10))))
