"""
    This object represents a square on a chess board
"""

import logging

from .queen import Queen

log = logging.getLogger('GA_Project')



class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.sum = 0
        self.queen = False
        return

    
    def place(self):
        self.queen = Queen(row=self.row, col=self.col)
        return


    def canCapture(self):
        self.sum += 1
        return