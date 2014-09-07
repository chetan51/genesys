import math

from classes.abstract_problem import AbstractProblem



class FitCurveProblem(AbstractProblem):

  INPUTS = ["x"]
  OUTPUTS = ["y"]
  OPERATORS = ["=", "+", "-", "*", "/"]
  CONSTANTS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


  @staticmethod
  def computeFitness(program):
    cost = 0.00001

    for x in xrange(50):
      results = program.run({"x": x})

      if "y" not in results:
        cost += 10000
        continue

      y = results["y"]
      cost += abs(y - FitCurveProblem._fn(x))

    return 100 * math.tanh(100 / cost)


  @staticmethod
  def _fn(x):
    return x + 4
