"""
    The main file for testing the Genetic Algorithms
    against the 8 Queens toy problem
"""

import logging
import os

from chessboard.board import Board
from RA.ra import RA
from GA_v1.ga import GA

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


def geneticAlgorithm():
    """ Runs genetic algorithm """
    # Config
    populationSize = 20
    ga = GA()

    # Generate initial population
    ga.generate(populationSize)
    ga.execute()

    #GA loop
    while not ga.solved:
        bestGenes = ga.select()
        ga.clear()
        ga.add(bestGenes)
        ga.generate(int(populationSize / 2))
        log.info(len(ga))

    
    """ This is how I want the selection and splicing loop to interface
    bestGenes = ga.select()
    bestGenes = ga.splice(bestGenes)
    ga.clear()
    ga.add(bestGenes)
    ga.generate(int(populationSize / 2))
    """
    return


def randomAgent():
    """
        Runs random agent
    """
    ra = RA()
    while ra.solved == False:
        ra.solve()


if __name__ == "__main__":
    # TODO: Run random agent
    geneticAlgorithm()

    # TODO: Record random agent results
    
    # TODO: Run genetic algorithm
    
    # TODO: Record genetic algorithm results
    #return