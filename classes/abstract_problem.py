class AbstractProblem(object):

  INPUTS = []
  OUTPUTS = []
  OPERATORS = []
  CONSTANTS = []


  def __init__(self, args=None):
    args = {} if args is None else args
    self.args = args


  @staticmethod
  def computeFitness(program):
    raise NotImplementedError()
