"""
    The random agent algorithm.
"""

import logging
from random import randint
from pymongo import MongoClient

from chessboard.board import Board

log = logging.getLogger('GA_Project')


class RA:
    """
    This is the Random Agent (RA) object. This algorithm randomly places Queens 
    on the Boards until it solves the 8 Queens problem. It is used as a control 
    variable to compare the performance of the Genetic Algorithms to.

    ...

    Attributes
    ----------
    solutions : int
        The number of attempts the (RA) has made to solve the problem
    isSolved : bool
        Whether or not the (RA) has solved the 8 Queens problem
    board : Board
        The virtual chess board

    Methods
    -------
    solve(self):
        Creates a Board and places the Queens
    isSolved(self):
        This function is called when the goal state is achieved
    storeResults(self):
        Stores results of RA in MongoDB
    """

    def __init__(self):
        self.solutions = 0 
        self.isSolved = False 
        self.board = None
        self.genome = []    
        return


    def solve(self):
        """Creates a Board and places the Queens"""

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
        """This function is called when the goal state is achieved"""

        self.storeResults()
        self.isSolved = True  # The last thing to run before return
        return


    def storeResults(self):
        """Stores results of RA in MongoDB"""

        # Create goalState dict
        goalState = {
            "genome": self.genome,
            "board": self.board,
            "sum": 0
        }

        # Connect to db
        try:
            client = MongoClient()
            db = client['ga_db']
            
            results = {
                "solutions": self.solutions,
                "genome": goalState
            }

            db['ra'].insert_one(results)
            
        except:
            log.error('Could not connect to MongoDB.')
            return
            
        return
