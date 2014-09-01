import random

from classes.node import Node
from classes.program import Program



class Population(object):

  GROWTH_FACTOR_SCALE = 0.5
  MAX_PROGRAM_DEPTH = 10


  def __init__(self, problem, size=100):
    self.size = size
    self.problem = problem
    self.programs = []

    self._createPrograms()


  def computeFitnesses(self):
    raise NotImplementedError()


  def killWeakest(self, n, fitnesses):
    raise NotImplementedError()


  def mateStrongest(self, n, fitnesses):
    raise NotImplementedError()


  def mutate(self):
    raise NotImplementedError()


  def getBest(self, fitnesses):
    raise NotImplementedError()


  def _createPrograms(self):
    for i in xrange(self.size):
      growthFactor = (float(i) / self.size) * Population.GROWTH_FACTOR_SCALE
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
