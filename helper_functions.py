#!/usr/bin/python

def print_bare_board(board):
    pretty = ''
    for row in board:
        for cell in row[:-1]:
            pretty += ' %d |' % cell
        pretty += ' %d \n' % row[-1]
    return pretty.replace('0', ' ')[:-1]
