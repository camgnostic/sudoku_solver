#!/usr/bin/python

import helper_functions as hf
import sample_puzzles as puzzles
import unittest
import mock

class TestPrintingFunctions(unittest.TestCase):
    def test_pretty_print_bare_board(self):
        puzzle = puzzles.medium_puzzle
        pretty = puzzles.pretty_medium_puzzle
        assert hf.print_bare_board(puzzle) == pretty, \
            '%s\n != \n%s' % (repr(pretty), repr(hf.print_bare_board(puzzle)))

class TestBasicHelpers(unittest.TestCase):
    def test_coordinates_to_square_coordinates(self):
        assert hf.cell_to_square(0, 0, 9) == (0, 0)
        assert hf.cell_to_square(2, 7, 9) == (0, 2)
        assert hf.cell_to_square(1, 3, 4) == (0, 1)

class TestRowFunctions(unittest.TestCase):
    unsolved_row = puzzles.medium_puzzle[0]
    solved_row = puzzles.medium_solution[0]

    def test_row_exists(self):
        row = hf.Row(self.unsolved_row)

    def test_row_identifies_unsolved(self):
        row = hf.Row(self.unsolved_row)
        assert not row.solved

    def test_row_identifies_solved(self):
        row = hf.Row(self.solved_row)
        assert row.solved

    def test_row_handles_tiny(self):
        tiny_row_solved = [1, 2, 3, 4]
        tiny_row_unsolved = [1, 2, 0, 4]
        solved_row = hf.Row(tiny_row_solved)
        assert solved_row.solved
        unsolved_row = hf.Row(tiny_row_unsolved)
        assert not unsolved_row.solved

class TestColumnFunctions(unittest.TestCase):
    unsolved_column = [row[0] for row in puzzles.medium_puzzle]
    solved_column = [row[0] for row in puzzles.medium_solution]

    def test_column_exists(self):
        column = hf.Column(self.unsolved_column)

    def test_column_identifies_unsolved(self):
        column = hf.Column(self.unsolved_column)
        assert not column.solved

    def test_column_identifies_solved(self):
        column = hf.Column(self.solved_column)
        assert column.solved

    def test_column_handles_tiny(self):
        tiny_col_solved = [1, 2, 3, 4]
        tiny_col_unsolved = [1, 2, 0, 4]
        solved_col = hf.Column(tiny_col_solved)
        assert solved_col.solved
        unsolved_col = hf.Column(tiny_col_unsolved)
        assert not unsolved_col.solved

class TestSquareFunctions(unittest.TestCase):
    whole_puzzle = puzzles.medium_puzzle
    square_0_2 = [[0,0,0], [0,0,0], [0,6,0]]
    square_1_1 = [[0,6,0], [8,0,3], [0,2,0]]
    square_0_2_values = [0,0,0,0,0,0,0,6,0]
    solved_square = hf.get_square(puzzles.medium_solution, 1, 1)
    unsolved_square = hf.get_square(puzzles.medium_puzzle, 1, 1)

    def test_square_values_identified(self):
        assert hf.get_square(self.whole_puzzle, 1, 1) == self.square_1_1, \
            '%s != %s' % (str(hf.get_square(self.whole_puzzle, 1, 1)), str(self.square_1_1))
        assert hf.get_square(self.whole_puzzle, 0, 2) == self.square_0_2, \
            '%s != %s' % (str(hf.get_square(self.whole_puzzle, 0, 2)), str(self.square_0_2))

    def test_square_values_from_array(self):
        assert hf.get_square_values(self.square_0_2) == self.square_0_2_values

    def test_tiny_square_values_identified(self):
        assert hf.get_square(puzzles.tiny_puzzle, 1, 0) == [[0, 0], [0, 4]], \
            hf.get_square(puzzles.tiny_puzzle, 1, 0)
        assert hf.get_square_values([[2, 0], [0, 3]]) == [2, 0, 0, 3]

    def test_square_exists(self):
        square = hf.Square(self.unsolved_square)

    def test_square_identifies_unsolved(self):
        square = hf.Square(self.unsolved_square)
        assert not square.solved

    def test_square_identifies_solved(self):
        square = hf.Square(self.solved_square)
        assert square.solved

    def test_square_handles_tiny(self):
        tiny_sq_solved = [[1, 2], [3, 4]]
        tiny_sq_unsolved = [[1, 2], [0, 4]]
        solved_sq = hf.Square(tiny_sq_solved)
        assert solved_sq.solved
        unsolved_sq = hf.Square(tiny_sq_unsolved)
        assert not unsolved_sq.solved

class TestSubBoard(unittest.TestCase):
    puzzle = puzzles.medium_puzzle
    def test_subboard_exists(self):
        subboard = hf.SubBoard(self.puzzle)

    def test_subboard_returns_row_and_col(self):
        row = self.puzzle[0]
        col = [r[3] for r in self.puzzle]
        square = hf.get_square_values(hf.get_square(self.puzzle, 2, 2))
        subboard = hf.SubBoard(self.puzzle)
        assert row == subboard.row[0].values
        assert col == subboard.col[3].values
        assert square == subboard.square[2][2].values

    def test_subboard_returns_row_and_col_and_square_for_cell(self):
        subboard = hf.SubBoard(self.puzzle)
        row = subboard.row[2]
        col = subboard.col[7]
        square = subboard.square[0][2]
        assert subboard.shadow(2, 7) == (row, col, square)
    
    def test_subboard_calls_remaining_on_cell_shadow(self):
        subboard = hf.SubBoard(self.puzzle)
        mock_cellset = mock.Mock()
        mock_cellset.remaining.return_value = 2
        mock_shadow = mock.Mock()
        mock_shadow.return_value = (mock_cellset, mock_cellset, mock_cellset)
        with mock.patch.object(subboard, 'shadow', mock_shadow):
            possibilities = subboard.get_possibilities(4, 3)


if __name__ == '__main__':
    unittest.main()
