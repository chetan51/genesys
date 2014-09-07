import random

from classes.node import Node



class Program(object):


  def __init__(self, root):
    self.root = root


  def run(self, assignments, maxOperations=1000, maxTime=1000):
    results = dict(assignments)

    try:
      Node.evaluate(self.root, results)
    except Exception as e:
      print "Error evaluating program: {0}".format(self.toString())
      raise e

    return results


  def mate(self, program):
    childA = Node.copy(self.root)
    childB = Node.copy(program.root)

    nodeA = random.choice(Node.traverseInOrder(childA))
    nodeB = random.choice(Node.traverseInOrder(childB))

    childA = Node.replace(childA, nodeA, nodeB)
    childB = Node.replace(childB, nodeB, nodeA)

    return [Program(childA), Program(childB)]


  def toString(self):
    return "{0} [{1} nodes]".format(Node.toString(self.root),
                                    len(Node.traverseInOrder(self.root)))
