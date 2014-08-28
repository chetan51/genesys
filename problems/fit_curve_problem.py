from classes.abstract_problem import AbstractProblem



class FitCurveProblem(AbstractProblem):

  TERMINALS = []
  OPERATORS = []
  INPUTS = []
  OUTPUTS = []


  def computeFitness(self, program):
    raise NotImplementedError()
