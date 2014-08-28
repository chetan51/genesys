class AbstractProblem(object):

  TERMINALS = []
  OPERATORS = []
  INPUTS = []
  OUTPUTS = []


  @staticmethod
  def computeFitness(program):
    raise NotImplementedError()
