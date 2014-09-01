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
    problem = FitCurveProblem()

    fitness = problem.computeFitness(program)
    self.assertEqual(fitness, 100)


  def testComputeFitnessLow(self):
    root = Node("=")
    root.left = Node("y")
    root.right = Node("4")

    program = Program(root)
    problem = FitCurveProblem()

    fitness = problem.computeFitness(program)
    self.assertEqual(fitness, 8.14518041038435)


if __name__ == "__main__":
  unittest.main()
