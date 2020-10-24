"""
    The first Genetic Algorithm
"""

import logging
from random import randint
from random import shuffle

from chessboard.board import Board

log = logging.getLogger('GA_Project')


class GA:

    def __init__(self):
        self.solutions = 0 # Number of solutions attempted
        self.solved = False # Was 8 Queens problems solved?
        self.population = [] # List of genome dictionaries.


    def __len__(self):
        return len(self.population)
        
    
    def generate(self, genome = None):
        """ 
            @params:
                genome = list of allele lists (Queen positions)

            Generate a random genome
        """

        # Generate genome dict from scratch
        if genome == None:
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
        self.solutions += 1
        return


    def add(self, genome):
        """ 
            Adds genome dictionary to population
        """

        self.population.append(genome)
        self.solutions += 1
        log.debug('Added {} to population'.format(genome['genome']))
        return


    def execute(self):
        """
            Places queens on the boards of the population
            based on their genomes
        """

        for genome in self.population:
            # Check if board is full
            if genome['board'].isFull:

                # Use coordinates in genome to place queens on board
                log.debug('Placing Queens on board')
                for gene in genome['genome']:
                    genome['board'].place(gene[0], gene[1])
                
                # Calculate fitness of genome
                genome['sum'] = genome['board'].getSum()
                log.debug('This solution has {} captures'.format(genome['sum']))

                # Add to solutions sum
                self.solutions += 1

                # If goal state achieved:
                if genome['sum'] == 0:
                    log.debug('Goal state has been achieved')
                    self.solved()

            else:
                log.debug('Queens already placed on this board. Skipping.')
        return


    def select(self):
        """
            Returns a subset of the population based on whatever
            selection algorithm
            @return list of genome dictionaries
        """

        # Sort population based on heuristic
        try:
            sortedPopulation = sorted(self.population, key = lambda i: i['sum'])

        except:
            log.error('Population could not be sorted.')
            sortedPopulation = []

        # Divide population by 2
        fittestPopulation = []
        for i in range(int(len(sortedPopulation) / 2)):
            fittestPopulation.append(sortedPopulation[i])
            log.debug('Fittest population genome sum: {}'.format(sortedPopulation[i]['sum']))

        return fittestPopulation


    def splice(self, population: list):
        """
            Takes selected genes and splices them based on whatever
            splicing algorithm. Returns list of genome dictionaries

            @return list of spliced genomes
        """

        splicedPopulation = []  # List of spliced genomes to be returned
        temp = []               # Temporary storage of alleles getting swapped
        geneOne = {}            # Gene on the splicing block
        geneTwo = {}            # Other gene on the splicing block

        # Randomize population order
        shuffle(population)

        # Splicing algorithm
        while len(population) > 1:
            geneOne['board'] = Board()
            geneTwo['board'] = Board()
            geneOne['genome'] = population.pop(0)['genome']
            geneTwo['genome'] = population.pop(0)['genome']

            for allele in range(len(geneOne)):
                # Coin toss
                coin = randint(0, 1)
                if coin:
                    temp = geneOne['genome'][allele]
                    geneOne['genome'][allele] = geneTwo['genome'][allele]
                    geneTwo['genome'][allele] = temp  

            splicedPopulation.append(geneOne)
            splicedPopulation.append(geneTwo)

        return splicedPopulation


    def clear(self):
        """
            Clears the population
        """
        self.population = []
        return


    def getPopulationStats(self):
        """
            Logs the statistics of the current population of genomes.
        """
        fitness = []
        for chromosome in self.population:
            fitness.append(chromosome['sum'])
        
        log.info('Size of population: {}'.format(len(self)))
        log.info('Average fitness: {}'.format((sum(fitness) / len(fitness))))
        return

    
    def getFittestStats(self):
        """
            Logs the statistics of the fittest half of the population
        """
        fittestPopulation = []
        fittestSums = []
        populationCopy = sorted(self.population, key = lambda i: i['sum'])
        # Gets the best half of the population
        for i in range(int(len(populationCopy) / 2)):
            fittestPopulation.append(populationCopy[i])
        
        # Gets the sums of the best half
        for chromosome in fittestPopulation:
            fittestSums.append(chromosome['sum'])

        log.info(fittestSums)
        log.info('Total conflicts of fittest population:'.format(sum(fittestSums)))
        return


    def solved(self):
        """
            This function is called when the goal state is achieved
        """
        # TODO: Figure out what to do.
        # Maybe record ga's stats to a csv, JSON object or mongodb cluster
        
        self.solved = True  # The last thing to run before return
        return
