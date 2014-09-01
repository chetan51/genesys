#! /usr/bin/env python

import unittest

from classes.population import Population
from problems.fit_curve_problem import FitCurveProblem



class PopulationTest(unittest.TestCase):


  def testInit(self):
    population = Population(FitCurveProblem, size=100)
    self.assertEqual(len(population.programs), 100)



if __name__ == "__main__":
  unittest.main()
