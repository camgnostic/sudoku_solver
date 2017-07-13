import unittest
import solve_tools
import sample_puzzles

# test that a single square -> single_square
# medium_step1 -> single choice
# medium_step2 -> single choice


class TestSingleChoice(unittest.TestCase):
    def test_single_choices_are_cleared(self):
        puzzle = sample_puzzles.medium_step1
        poss_map = solve_tools.get_possibility_map(puzzle)
        self.assertEqual(solve_tools.unmap(solve_tools.solve_single_choice(poss_map)), sample_puzzles.medium_step2)


class TestSinglePossibleOverall(unittest.TestCase):
    def test_single_possible_finds_spot(self):
        puzzle = solve_tools.get_possibility_map(sample_puzzles.single_square1)
        next_puzzle = sample_puzzles.single_square2
        self.assertEqual(solve_tools.unmap(solve_tools.solve_single_spot(puzzle)), next_puzzle)
