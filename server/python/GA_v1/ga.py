"""
    The first Genetic Algorithm
"""

import logging
from random import randint

from chessboard.board import Board

log = logging.getLogger('GA_Project')


class GA:

    def __init__(self):
        self.solutions = 0 # Number of solutions attempted
        self.solved = False # Was 8 Queens problems solved?
        self.genes = [] 
        
    
    def generatePopulation(self, populationSize=20):
        """ Generate initial population """

        for i in range(populationSize):
            # Create genome
            genome = []
            for i in range(8):
                genome.append([i, randint(0, 7)])
            log.debug('New genome generated: \n \
                {}'.format(genome))

            # Create gene dict
            newGene = {
                "board": Board(),
                "genome": genome
            }

            # Append to genes
            self.genes.append(newGene)
        return
    
