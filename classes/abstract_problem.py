class AbstractProblem(object):

  INPUTS = []
  OUTPUTS = []
  OPERATORS = []
  CONSTANTS = []


  def __init__(self, args=None):
    args = {} if args is None else args
    self.args = args


  def computeFitness(self, program):
    raise NotImplementedError()
