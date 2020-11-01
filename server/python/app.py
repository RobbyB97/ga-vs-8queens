"""
    The main file for testing the Genetic Algorithms
    against the 8 Queens toy problem
"""

import logging
import os
from time import sleep
from pymongo import MongoClient

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


def geneticAlgorithm1():
    """ Runs genetic algorithm (version 1) """
    # Config
    populationSize = 20
    ga = GA()

    # Generate initial population
    log.debug('Generating initial population.')
    for i in range(populationSize):
        ga.generate()
    
    log.debug('Executing genomes in population')
    ga.execute()

    log.debug('Printing sums of population')
    for genome in ga.population:
        log.debug(genome['sum'])

    #GA loop
    # TODO: The logic of what to do when goal state is achieved needs to be ironed out
    while not ga.solved:
        ga.nextGeneration()
        bestGenes = []
        splicedGenes = []

        # Selection
        bestGenes = ga.select()
        log.debug('Here are the best genes: {}'.format(bestGenes))
        ga.clear()

        # TODO: Recombination
        splicedGenes = ga.splice(bestGenes)
        for chromosome in splicedGenes:
            ga.add(chromosome)
        
        # Replenish population
        log.debug('Replenishing population')
        for i in range(int(populationSize / 2)):
            log.debug('Generating new genome')
            ga.generate()

        # Execute new genomes
        ga.execute()
        sleep(1)
    return


def randomAgent():
    """ Runs random agent """
    ra = RA()
    while ra.solved == False:
        ra.solve()
    return


if __name__ == "__main__":
    # Generate 10,000 solutions with the RA and GA
    for i in range(10000):
        randomAgent()
        geneticAlgorithm1()
    return