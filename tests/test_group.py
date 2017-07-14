#!/usr/bin/python3

import unittest
import group
import copy

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


square_test = [[1]*3 + [2]*3 + [3]*3]*3 + [[4]*3 + [5]*3 + [6]*3]*3 + [[7]*3 + [8]*3 + [9]*3]*3


class TestSquareGetter(unittest.TestCase):
    def test_correct_square_is_returned(self):
        assert group.get_square(0, square_test) == [1]*9

    def test_correct_square_after_first(self):
        assert group.get_square(1, square_test) == [2]*9

    def test_correct_square_middle_row(self):
        assert group.get_square(3, square_test) == [4]*9

    def test_correct_square_bottom_row(self):
        assert group.get_square(7, square_test) == [8]*9


class TestSquareGetter(unittest.TestCase):
    def setUp(self):
        self.square_test_copy = copy.deepcopy(square_test)

    def tearDown(self):
        self.square_test_copy = None

    def test_square_setter_first_square(self):
        assert group.get_square(0, group.set_square(0, self.square_test_copy,
                                                    ["a"]*9)) == ["a"]*9

    def test_square_setter_middle_square(self):
        assert group.get_square(5, group.set_square(5, self.square_test_copy,
                                                    ["a"]*9)) == ["a"]*9
