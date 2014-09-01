class Program(object):


  def __init__(self, root):
    self.root = root


  def run(self, assignments, maxOperations=1000, maxTime=1000):
    results = dict(assignments)
    Program._evaluate(self.root, results)
    return results


  def mate(self, program):
    raise NotImplementedError()


  def toString(self):
    return "{0} [{1} nodes]".format(Program._toString(self.root),
                                    len(Program._traverseInOrder(self.root)))


  @staticmethod
  def _evaluate(node, results):
    if node == None:
      return None

    if node.isTerminal():
      return Program._evaluatedValue(node, results)

    if node.value == "=":
      right = Program._evaluate(node.right, results)
      if node.left.isVariable() and right is not None:
        results[node.left.value] = right
      return None

    left = Program._evaluate(node.left, results)
    right = Program._evaluate(node.right, results)

    if node.value == "+":
      return left + right

    if node.value == "-":
      return left - right

    if node.value == "*":
      return left * right

    if node.value == "/":
      return left / right


  @staticmethod
  def _evaluatedValue(node, results):
    value = node.value
    if node.isVariable():
      value = results[node.value]

    return float(value)


  @staticmethod
  def _toString(root):
    if root is None:
      return ""

    if root.isTerminal():
      return root.value

    return "({0} {1} {2})".format(root.value,
                                  Program._toString(root.left),
                                  Program._toString(root.right))


  @staticmethod
  def _traverseInOrder(root):
    if root is None:
      return []

    return ([root] +
            Program._traverseInOrder(root.left) +
            Program._traverseInOrder(root.right))
