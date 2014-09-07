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


  def testReplace(self):
    node = Node("1")
    node.left = Node("2")
    node.right = Node("3")
    node.left.left = Node("4")

    value = Node("5")
    node = Node.replace(node, node.left, value)

    self.assertEqual(node.value, "1")
    self.assertEqual(node.left.value, "5")
    self.assertEqual(node.right.value, "3")


  def testReplaceRoot(self):
    node = Node("1")
    node.left = Node("2")
    node.right = Node("3")
    node.left.left = Node("4")

    value = Node("5")
    node = Node.replace(node, node, value)

    self.assertEqual(node.value, "5")
    self.assertIsNone(node.left)
    self.assertIsNone(node.right)



if __name__ == "__main__":
  unittest.main()
