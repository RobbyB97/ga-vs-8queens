"""
    The main file for testing the Genetic Algorithms
    against the 8 Queens toy problem
"""

import logging
import os

from chessboard.board import Board

# Set logger
log = logging.getLogger('GA_Project')
log.setLevel(logging.INFO)
handlerpath = os.path.dirname(os.path.realpath(__file__)) + '/app.log'
handler = logging.FileHandler(handlerpath)
handler.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s]: %(message)s')
handler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)
log.addHandler(handler)



if __name__ == "__main__":
    x = Board()
    x.place(6,6)
    
    # TODO: Run random agent

    # TODO: Record random agent results
    
    # TODO: Run genetic algorithm
    
    # TODO: Record genetic algorithm results
    #return