import unittest
import solve_tools
import sample_puzzles


@unittest.skip('building subunits')
class TestSinglePossibleOverall(unittest.TestCase):
    def test_single_possible_finds_spot(self):
        puzzle = sample_puzzles.medium_step1
        next_puzzle = sample_puzzles.medium_step2
        self.assertEqual(solve_tools.solve_single_spot(puzzle), next_puzzle)
