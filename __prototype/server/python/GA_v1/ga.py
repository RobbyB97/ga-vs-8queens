"""
    The first Genetic Algorithm
"""

import logging
from random import randint
from random import shuffle
from pymongo import MongoClient

from chessboard.board import Board

log = logging.getLogger('GA_Project')


class GA:
    """
    This is the first iteration of the Genetic Algorithm (GA). The 'genome' is the
    coordinates of the Queens on the Board, with each Queen being one 'gene'.
    The best 'chromosomes' in a 'population' are spliced together, meaning the
    coordinates of some Queens on one solution are traded with another solution.
    These new solutions are dumped back into the population. Rinse and repeat 
    until the 8 Queens problem is solved.

    ...

    Attributes
    ----------
    solutions : int
        The number of attempts the GA has made to solve the problem
    generation : int
        The number of 'generations' the GA has generated
    isSolved : bool
        Whether or not the GA has solved the 8 Queen's problem
    population : list


    Methods
    -------
    solve(self):
        Creates a Board and places the Queens
    solved(self):
        This function is called when the goal state is achieved
    storeResults(self):
        Stores results of RA in MongoDB
    """

    def __init__(self):
        self.solutions = 0      # Number of solutions attempted
        self.generation = 0    # Number of generations passed
        self.isSolved = False     # Was 8 Queens problems solved?
        self.population = []    # List of genome dictionaries.
        self.goalState: dict = None   # Genome object that has achieved goalState


    def __len__(self):
        """
        The length of the GA = the length of the population
        
        Returns
        -------
        int
            The length of the population
        """
        return len(self.population)

   
    def generate(self, genome = None):
        """Generates a random genome"""

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
        """Adds genome dictionary to population"""

        self.population.append(genome)
        self.solutions += 1
        log.debug('Added {} to population'.format(genome['genome']))
        return


    def execute(self):
        """
        Places queens on the boards of the population based on their genomes
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
                    self.goalState = genome
                    self.solved()

            else:
                log.debug('Queens already placed on this board. Skipping.')
        return


    def select(self):
        """
        Returns a subset of the population based on whatever selection algorithm
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
        Takes selected genes and splices them based on whatever splicing 
        algorithm.

        ...

        Parameters
        ----------
        population : list
            The list of genomes that need to be spliced

        Returns
        -------
        list 
            A list of spliced genomes
        """

        splicedPopulation = []  # List of spliced genomes to be returned
        temp = []               # Temporary storage of alleles getting swapped
        geneOne = {}            # Gene on the splicing block
        geneTwo = {}            # Other gene on the splicing block

        # Randomize population order
        shuffle(population)

        # Splicing algorithm
        while len(population) > 1:
            old_geneOne = population.pop(0)
            old_geneTwo = population.pop(0)
            geneOne['board'] = Board()
            geneTwo['board'] = Board()
            geneOne['genome'] = old_geneOne['genome']
            geneTwo['genome'] = old_geneTwo['genome']

            for allele in range(len(geneOne)):
                # Check the coordinates of the allele
                # If neither queen can capture another piece: 25% chance of splice (1 in 4)
                # If one of the queens can capture another piece: 50% chance of splice (2 in 4)
                # If both queens can capture another piece: 75% chance of splice (3 in 4)

                # Calculate chance of splice
                odds_of_splice = 8
                
                # Check if Queens can capture other piece
                geneOne_canCapture = True
                geneTwo_canCapture = True
                geneOne_coords = geneOne['genome'][allele]
                geneTwo_coords = geneTwo['genome'][allele]
                
                if (old_geneOne['board'].canCapture(geneOne_coords) and old_geneTwo['board'].canCapture(geneTwo_coords)):
                    log.debug('Both queens can capture')
                    odds_of_splice -= 5
                
                elif (old_geneOne['board'].canCapture(geneOne_coords) or old_geneTwo['board'].canCapture(geneTwo_coords)):
                    log.debug('One queen can capture')
                    odds_of_splice -= 4

                # Coin toss
                coin = randint(1, odds_of_splice)
                if coin < 3:
                    log.debug('Gene spliced')
                    temp = geneOne['genome'][allele]
                    geneOne['genome'][allele] = geneTwo['genome'][allele]
                    geneTwo['genome'][allele] = temp  
                else:
                    log.debug('Gene not spliced.')

            splicedPopulation.append(geneOne)
            splicedPopulation.append(geneTwo)

        return splicedPopulation


    def clear(self):
        """Clears the population"""
        self.population = []
        return


    def nextGeneration(self):
        """Increments generation"""
        self.generation += 1
        return


    def getPopulationStats(self):
        """Logs the statistics of the current population of genomes"""
        fitness = []
        for chromosome in self.population:
            fitness.append(chromosome['sum'])
        
        log.info('Size of population: {}'.format(len(self)))
        log.info('Average fitness: {}'.format((sum(fitness) / len(fitness))))
        return

    
    def getFittestStats(self):
        """Logs the statistics of the fittest half of the population"""
        # Create lists to store the fittest of the population
        fittestPopulation = []
        fittestSums = []
        populationCopy = sorted(self.population, key = lambda i: i['sum'])

        # Gets the best half of the population
        for i in range(int(len(populationCopy) / 2)):
            fittestPopulation.append(populationCopy[i])
        
        # Gets the sums of the best half
        for chromosome in fittestPopulation:
            fittestSums.append(chromosome['sum'])

        # FIXME: sum(fittestSums) used in the log.info below returns null

        log.info(fittestSums)
        log.info('Total conflicts of fittest population: {}'.format(sum(fittestSums)))
        return


    def solved(self):
        """This function is called when the goal state is achieved"""
        self.isSolved = True  # The last thing to run before return
        return


    def storeResults(self):
        """Stores the results of the GA in MongoDB"""
        # Connect to db
        try:
            client = MongoClient()
            db = client['ga_db']
        except:
            log.error('Could not connect to MongoDB.')
            return

        # Gather results
        results = {
            "solutions": int(self.solutions),
            "genome": self.goalState,
            "generation": self.generation
        }

        # Post
        try:
            db['ga1'].insert_one(results)
            log.debug('Posted results to MongoDB.')
        except:
            log.error('Could not post results to MongoDB.')
        return