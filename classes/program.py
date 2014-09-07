from classes.node import Node



class Program(object):


  def __init__(self, root):
    self.root = root


  def run(self, assignments, maxOperations=1000, maxTime=1000):
    results = dict(assignments)
    Node.evaluate(self.root, results)
    return results


  def mate(self, program):
    raise NotImplementedError()


  def copy(self):
    root = Node.copy(self.root)
    return Program(root)


  def toString(self):
    return "{0} [{1} nodes]".format(Node.toString(self.root),
                                    len(Node.traverseInOrder(self.root)))
