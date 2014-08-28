class Population(object):


  def __init__(self, problem, size=100):
    self.size = size
    self.problem = problem


  def computeFitnesses(self):
    raise NotImplementedError()


  def killWeakest(self, n):
    raise NotImplementedError()


  def mateStrongest(self, n):
    raise NotImplementedError()


  def mutate(self):
    raise NotImplementedError()


  def getBest(self):
    raise NotImplementedError()


  @staticmethod
  def _createProgram(problem):
    raise NotImplementedError()
