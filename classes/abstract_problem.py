class AbstractProblem(object):

  TERMINALS = []
  OPERATORS = []
  INPUTS = []
  OUTPUTS = []


  def __init__(self, args):
    self.args = args


  def computeFitness(self, program):
    raise NotImplementedError()
