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
        self.population = [] # List of genome dictionaries.


    def __len__(self):
        return len(self.population)
        
    
    def generate(self, population=1):
        """ 
            Generate a random genome
        """
        for genome in range(population):
            # Create genome (Queen's coordinates on board)
            genome = []
            for i in range(8):
                # each gene = [i, random number between 0-7]
                genome.append([i, randint(0, 7)])
            
            log.debug('New genome generated: \n \
                {}'.format(genome))

            # Create the board
            genomeDict = {
                "board": Board(),
                "genome": genome,
                "sum": None
            }
            
            # Add new genome to population
            self.population.append(genomeDict)
        return


    def add(self, genomes = []):
        """ 
            Adds list of genome dictionaries
        """
        for genome in genomes:
            self.population.append(genome)
        return

    def execute(self):
        """
            Places queens on the boards of the population
            based on their genomes
        """

        for genome in self.population:
            # Use coordinates in genome to place queens on board
            for gene in genome['genome']:
                genome['board'].place(gene[0], gene[1])
            
            # Calculate fitness of genome
            genome['sum'] = genome['board'].getSum()
            log.debug('This solution has {} captures'.format(genome['sum']))

        # TODO: Check for goal state
        return


    def select(self):
        """
            Returns a subset of the population based on whatever
            selection algorithm
            @return list of genome dictionaries
        """

        # Sort population based on heuristic
        sortedPopulation = sorted(self.population, key = lambda i: i['sum'])

        # Divide population by 2
        fittestPopulation = []
        for i in range(int(len(sortedPopulation) / 2)):
            fittestPopulation.append(sortedPopulation[i])
        return fittestPopulation


    def splice(self, population):
        """
            Takes selected genes and splices them based on whatever
            splicing algorithm. Returns list of genome dictionaries
        """
        # TODO
        return population


    def clear(self):
        """
            Clears the population
        """
        self.population = []
        return
