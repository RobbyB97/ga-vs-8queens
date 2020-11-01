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
        self.genome = []    
        return


    def solve(self):
        """ 
            Creates a board and places queens 
            Returns true if solution was found    
        """

        # Generate board
        self.board = Board()
        self.genome = []    # Reset genome
        for i in range(8):
            col = randint(0, 7)
            allele = [1, col]
            log.debug('Placing Queen at [{}, {}]'.format(i, col))
            self.board.place(i, col)
            self.genome.append(allele)
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
        self.storeResults()
        self.solved = True  # The last thing to run before return
        return


    def storeResults(self):
        """ Stores results of RA in MongoDB """
        
        # Connect to db
        try:
            client = MongoClient()
            db = client['ga_db']
            
            post = {
                "solutions": self.solutions,
                "genome": self.genome
            }

            db['ra'].insert_one(post)
            
        except:
            log.error('Could not connect to MongoDB.')
            return
            
        return
