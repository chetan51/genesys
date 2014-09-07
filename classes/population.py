import numpy
import random

from classes.node import Node
from classes.program import Program



class Population(object):

  GROWTH_FACTOR_SCALE = 0.5
  MAX_PROGRAM_DEPTH = 10
  MUTATION_PROBABILITY = 0.01


  def __init__(self, problem, size=100):
    self.problem = problem
    self.programs = []

    self._createPrograms(size)


  def size(self):
    return len(self.programs)


  def computeFitnesses(self):
    fitnesses = dict()

    for program in self.programs:
      fitnesses[program] = self.problem.computeFitness(program)

    return fitnesses


  def killWeakest(self, n, fitnesses):
    sortedPrograms = self.sortProgramsByFitness(fitnesses)
    keep = max(0, self.size() - n)
    self.programs = sortedPrograms[0:keep]


  def mateStrongest(self, n, fitnesses):
    sortedPrograms = self.sortProgramsByFitness(fitnesses)
    for i in xrange(0, n/2):
      children = sortedPrograms[i].mate(sortedPrograms[i+1])
      self.programs += children


  def mutate(self):
    for program in self.programs:
      for node in Node.traverseInOrder(program.root):
        if random.random() < self.MUTATION_PROBABILITY:
          if node.isTerminal():
            node.value = self._createTerminalNode(self.problem).value
          else:
            node.value = self._createOperatorNode(self.problem).value


  def sortProgramsByFitness(self, fitnesses):
    def breakTiesRandomly(a, b):
      diff = cmp(a, b)
      return diff if diff else random.choice([-1, 1])

    sortedFitnesses = sorted(fitnesses.iteritems(),
                             key=lambda (k, v): v,
                             cmp=breakTiesRandomly,
                             reverse=True)
    sortedPrograms = [k for (k, v) in sortedFitnesses]
    return sortedPrograms


  def computeFitnessStats(self, fitnesses):
    """
		@return (tuple) stats (min, max, average, standard deviation)
		"""
    scores = numpy.array(fitnesses.values())
    return (scores.min(), scores.max(), scores.mean(), scores.std())


  def _createPrograms(self, size):
    for i in xrange(size):
      growthFactor = (float(i) / size) * Population.GROWTH_FACTOR_SCALE
      self.programs.append(Population._createProgram(self.problem, growthFactor))


  @staticmethod
  def _createProgram(problem, growthFactor):
    """
    @param (float) growthFactor: Probability of creating an operator instead
                                 of a terminal, thereby extending the tree
    """
    root = Population._createNode(problem, growthFactor)
    return Program(root)


  @staticmethod
  def _createNode(problem, growthFactor, depth=0):
    node = None

    if depth == Population.MAX_PROGRAM_DEPTH:
      return node

    if random.random() < growthFactor:
      node = Population._createOperatorNode(problem)
      node.left = Population._createNode(problem, growthFactor, depth+1)
      node.right = Population._createNode(problem, growthFactor, depth+1)
    else:
      node = Population._createTerminalNode(problem)

    return node


  @staticmethod
  def _createOperatorNode(problem):
    candidates = problem.OPERATORS
    return Node(random.choice(candidates))


  @staticmethod
  def _createTerminalNode(problem):
    candidates = problem.INPUTS + problem.OUTPUTS + problem.CONSTANTS
    return Node(random.choice(candidates))
