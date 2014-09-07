#! /usr/bin/env python

import unittest

from classes.node import Node
from classes.program import Program
from problems.fit_curve_problem import FitCurveProblem



class FitCurveProblemTest(unittest.TestCase):


  def testComputeFitnessHigh(self):
    root = Node("=")
    root.left = Node("y")
    root.right = Node("+")
    root.right.left = Node("x")
    root.right.right = Node("4")

    program = Program(root)

    fitness = FitCurveProblem.computeFitness(program)
    self.assertEqual(fitness, 100)


  def testComputeFitnessLow(self):
    root = Node("=")
    root.left = Node("y")
    root.right = Node("4")

    program = Program(root)

    fitness = FitCurveProblem.computeFitness(program)
    self.assertEqual(fitness, 8.14518041038435)


  def testComputeFitnessDOA(self):
    root = Node("=")
    root.left = Node("x")
    root.right = Node("4")

    program = Program(root)

    fitness = FitCurveProblem.computeFitness(program)
    self.assertEqual(fitness, 0.019999999732933336)


if __name__ == "__main__":
  unittest.main()
