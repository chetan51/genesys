#! /usr/bin/env python

import unittest

from classes.node import Node
from classes.program import Program



class ProgramTest(unittest.TestCase):


  def testRun(self):
    root = Node("=")
    root.left = Node("y")
    root.right = Node("+")
    root.right.left = Node("x")
    root.right.right = Node("4")

    program = Program(root)
    result = program.run({"x": 3})

    self.assertEqual(result["x"], 3)
    self.assertEqual(result["y"], 7)


  def testRunSelfReferencingVariable(self):
    root = Node("=")
    root.left = Node("y")
    root.right = Node("+")
    root.right.left = Node("y")
    root.right.right = Node("3")

    program = Program(root)
    result = program.run({"y": 2})

    self.assertEqual(result["y"], 5)


  def testCopy(self):
    programA = ProgramTest._createProgram()
    programB = programA.copy()

    self.assertEqual(programA.toString(), programB.toString())


  @staticmethod
  def _createProgram():
    root = Node("=")
    root.left = Node("y")
    root.right = Node("+")
    root.right.left = Node("y")
    root.right.right = Node("3")

    return Program(root)


if __name__ == "__main__":
  unittest.main()
