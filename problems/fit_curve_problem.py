from classes.abstract_problem import AbstractProblem

class FitCurveProblem(AbstractProblem):

  TERMINALS = []
  OPERATORS = []
  INPUTS = []
  OUTPUTS = []


  @staticmethod
  def computeFitness(program):
    raise NotImplementedError()
