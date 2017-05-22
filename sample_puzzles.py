#!/usr/bin/python

# FUNCTIONAL PUZZLE TESTS:
solved9 = [
    [9, 2, 6, 5, 8, 3, 4, 7, 1],
    [7, 1, 3, 4, 2, 6, 9, 8, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 7, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [6, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7]
]

solved4 = [
    [4, 2, 3, 1],
    [3, 1, 4, 2],
    [1, 3, 2, 4],
    [2, 4, 1, 3]
]

one_square = {
    'large': {
        'solution': solved9,
        'corner':
            [
                [9, 2, 6, 5, 8, 3, 4, 7, 0],
                [7, 1, 3, 4, 2, 6, 9, 8, 5],
                [8, 4, 5, 9, 7, 1, 3, 6, 2],
                [3, 6, 2, 8, 5, 7, 1, 4, 9],
                [4, 7, 1, 2, 6, 9, 5, 3, 8],
                [5, 9, 8, 3, 1, 4, 7, 2, 6],
                [6, 5, 7, 1, 3, 8, 2, 9, 4],
                [2, 8, 4, 7, 9, 5, 6, 1, 3],
                [1, 3, 9, 6, 4, 2, 8, 5, 7]
            ],
        'edge':
            [
                [9, 2, 6, 5, 8, 3, 4, 7, 1],
                [7, 1, 3, 4, 2, 6, 9, 8, 5],
                [8, 4, 5, 9, 7, 1, 3, 6, 2],
                [3, 6, 2, 8, 5, 7, 1, 4, 9],
                [4, 7, 1, 2, 6, 9, 5, 3, 8],
                [5, 9, 8, 3, 1, 4, 7, 2, 6],
                [6, 5, 7, 1, 3, 8, 2, 9, 4],
                [2, 8, 4, 7, 9, 5, 6, 1, 3],
                [1, 3, 9, 6, 0, 2, 8, 5, 7]
            ],
        'middle':
            [
                [9, 2, 6, 5, 8, 3, 4, 7, 1],
                [7, 1, 3, 4, 2, 6, 9, 8, 5],
                [8, 4, 5, 9, 7, 1, 3, 6, 2],
                [3, 6, 2, 8, 5, 7, 1, 4, 9],
                [4, 7, 1, 2, 0, 9, 5, 3, 8],
                [5, 9, 8, 3, 1, 4, 7, 2, 6],
                [6, 5, 7, 1, 3, 8, 2, 9, 4],
                [2, 8, 4, 7, 9, 5, 6, 1, 3],
                [1, 3, 9, 6, 4, 2, 8, 5, 7]
            ],
    },
    'small': {
        'solution': solved4,
        'corner':
            [
                [4, 2, 3, 1],
                [3, 1, 4, 2],
                [1, 3, 2, 4],
                [2, 4, 1, 0]
            ],
        'edge':
            [
                [4, 2, 3, 1],
                [3, 1, 4, 2],
                [1, 3, 2, 4],
                [2, 0, 1, 3]
            ],
        'middle':
            [
                [4, 2, 3, 1],
                [3, 1, 4, 2],
                [1, 3, 0, 4],
                [2, 4, 1, 3]
            ]
    }
}

two_missing = [
    [9, 0, 6, 5, 8, 3, 4, 7, 1],
    [7, 1, 0, 4, 2, 6, 9, 8, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 7, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [6, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7]]


simple_puzzle = [
    [9, 0, 6, 5, 8, 3, 4, 7, 1],
    [7, 1, 0, 4, 2, 6, 9, 8, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 7, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [6, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7]]

simple_solution = [
    [9, 2, 6, 5, 8, 3, 4, 7, 1],
    [7, 1, 3, 4, 2, 6, 9, 8, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 7, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [6, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7]]

single_spot_puzzle = [
    [0, 0, 6, 5, 8, 3, 4, 7, 1],
    [0, 0, 3, 4, 2, 0, 0, 0, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 0, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [0, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7]
]

medium_puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]]

medium_solution = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]]

difficult_puzzle = [
    [9, 0, 0, 0, 8, 0, 0, 0, 1],
    [0, 0, 0, 4, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 7, 0, 3, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [4, 0, 1, 0, 6, 0, 5, 0, 8],
    [0, 9, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 7, 0, 3, 0, 2, 0, 0],
    [0, 0, 0, 7, 0, 5, 0, 0, 0],
    [1, 0, 0, 0, 4, 0, 0, 0, 7]]

difficult_solution = [
    [9, 2, 6, 5, 8, 3, 4, 7, 1],
    [7, 1, 3, 4, 2, 6, 9, 8, 5],
    [8, 4, 5, 9, 7, 1, 3, 6, 2],
    [3, 6, 2, 8, 5, 7, 1, 4, 9],
    [4, 7, 1, 2, 6, 9, 5, 3, 8],
    [5, 9, 8, 3, 1, 4, 7, 2, 6],
    [6, 5, 7, 1, 3, 8, 2, 9, 4],
    [2, 8, 4, 7, 9, 5, 6, 1, 3],
    [1, 3, 9, 6, 4, 2, 8, 5, 7]]

tiny_puzzle = [
    [4, 0, 3, 0],
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 4, 0, 3]
]

tiny_solution = [
    [4, 2, 3, 1],
    [3, 1, 4, 2],
    [1, 3, 2, 4],
    [2, 4, 1, 3]
]

tiny_insoluble = [
    [4, 2, 3, 1],
    [3, 0, 4, 2],
    [0, 1, 2, 4],
    [2, 4, 1, 3]
]

# FORMATTING / PRINTING:
pretty_medium_puzzle = '\n'.join([
 ' 5 | 3 |   |   | 7 |   |   |   |   ',
 ' 6 |   |   | 1 | 9 | 5 |   |   |   ',
 '   | 9 | 8 |   |   |   |   | 6 |   ',
 ' 8 |   |   |   | 6 |   |   |   | 3 ',
 ' 4 |   |   | 8 |   | 3 |   |   | 1 ',
 ' 7 |   |   |   | 2 |   |   |   | 6 ',
 '   | 6 |   |   |   |   | 2 | 8 |   ',
 '   |   |   | 4 | 1 | 9 |   |   | 5 ',
 '   |   |   |   | 8 |   |   | 7 | 9 '])
