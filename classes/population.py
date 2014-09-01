class Population(object):


  def __init__(self, problem, size=100):
    self.size = size
    self.problem = problem


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


  @staticmethod
  def _createProgram(problem):
    raise NotImplementedError()
