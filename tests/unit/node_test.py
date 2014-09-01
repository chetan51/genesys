#! /usr/bin/env python

import unittest

from classes.node import Node



class NodeTest(unittest.TestCase):


  def testIsVariablePositive(self):
    self.assertTrue(Node("x").isVariable())
    self.assertTrue(Node("xx").isVariable())
    self.assertTrue(Node("x4").isVariable())


  def testIsVariableNegative(self):
    self.assertFalse(Node("3").isVariable())
    self.assertFalse(Node("3.5").isVariable())
    self.assertFalse(Node("=").isVariable())



if __name__ == "__main__":
  unittest.main()
