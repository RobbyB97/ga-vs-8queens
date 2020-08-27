"""
    This is the chess board object.
"""

import logging

from .square import Square

log = logging.getLogger('GA_Project')



class Board:
    def __init__(self):
        # Create the chess board
        self.board = []
        self.sum = 0

        for row in range(8):
            row = []
            for col in range(8):
                row.append(Square(row=row, col=col))
            self.board.append(row)


    def place(self, row, col):
        # Place Queen
        self.board[row][col].place()

        # TODO: Find North/South capturable squares
        
        # TODO: Find East/West capturable squares

        # TODO: Find NE capturable squares

        # TODO: Find NW capturable squares

        # TODO: Find SE capturable squares

        # TODO: Find SW capturable squares
        return