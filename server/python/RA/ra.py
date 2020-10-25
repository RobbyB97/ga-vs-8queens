"""
    The random agent algorithm.
"""

import logging
from random import randint
from pymongo import MongoClient

from chessboard.board import Board

log = logging.getLogger('GA_Project')


class RA:

    def __init__(self):
        self.solutions = 0 # Number of solutions attempted
        self.solved = False # Was 8 Queens problem solved?
        self.board = None
        self.storeResults()
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
            log.debug('Random agent solved 8 Queens problem in {} attempts'.format(self.solutions))
            self.solved()

        else:
            log.debug('Random agent generated solution with {} conflicts'.format(self.board.getSum()))
        return


    def solved(self):
        """ 
            This function is called when the goal state is achieved 
        """

        self.solved = True  # The last thing to run before return
        return


    def storeResults(self):
        """ Stores results of RA in MongoDB """
        
        # Connect to db
        try:
            client = MongoClient()
            db = client.ga_db
            ra_db = db.ra
        except:
            log.error('Could not connect to MongoDB.')
            return

        # Gather results
        results = {
            "attempts": int(self.solutions),
            "queens": self.board.getQueens()
        }

        # Post
        try:
            ra_db.insert_one(results)
            log.debug('Posted results to MongoDB.')
        except:
            log.error('Could not post results to MongoDB.')
        return
