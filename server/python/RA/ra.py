"""
    The random agent algorithm.
"""

import logging
from random import randint

from chessboard.board import Board

log = logging.getLogger('GA_Project')


class RA:

    def __init__(self):
        self.solutions = 0 # Number of solutions attempted
        self.solved = False # Was 8 Queens problem solved?
        self.board = None
        return


    def solve(self):
        """ 
            Creates a board and places queens 
            Returns true if solution was found    
        """

        # Generate board
        self.board = Board()
        for i in range(8):
            col = randint(0, 7)
            log.debug('Placing Queen at [{}, {}]'.format(i, col))
            self.board.place(i, col)
        self.solutions += 1
        
        # Test fitness
        if self.board.getSum == 0:
            log.info('Random agent solved 8 Queens problem in {} attempts'.format(self.solutions))
            self.solved = True
        return

    
