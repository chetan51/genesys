#! /usr/bin/env python

import random
import unittest

from classes.population import Population
from problems.fit_curve_problem import FitCurveProblem



class PopulationTest(unittest.TestCase):


  def setUp(self):
    random.seed(42)


  def testInit(self):
    population = Population(FitCurveProblem, size=100)
    self.assertEqual(population.size(), 100)


  def testComputeFitnesses(self):
    population = Population(FitCurveProblem, size=100)
    fitnesses = population.computeFitnesses()
    self.assertEqual(len(fitnesses), 100)


  def testKillWeakest(self):
    population = Population(FitCurveProblem, size=100)
    fitnesses = population.computeFitnesses()
    population.killWeakest(20, fitnesses)
    self.assertEqual(population.size(), 80)


  def testMateStrongest(self):
    population = Population(FitCurveProblem, size=100)
    fitnesses = population.computeFitnesses()
    population.mateStrongest(11, fitnesses)
    self.assertEqual(population.size(), 110)



if __name__ == "__main__":
  unittest.main()
