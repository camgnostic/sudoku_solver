#!/usr/bin/python

import main_class as mc
import unittest
import sample_puzzles as puzzles

class TestBoardClass(unittest.TestCase):
    def test_class_exists(self):
        board = mc.Board
        
    def test_board_loads_puzzle(self):
        board = mc.Board(puzzles.simple_puzzle)


if __name__ == '__main__':
    unittest.main()
