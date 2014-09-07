class Node(object):


  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


  def isTerminal(self):
    value = self.value

    return (value is not None and
            value != "=" and
            value != "+" and
            value != "-" and
            value != "*" and
            value != "/")


  def isVariable(self):
    if not self.isTerminal():
      return False

    try:
      float(self.value)
    except ValueError:
      return True

    return False


  @staticmethod
  def evaluate(node, results):
    if node is None:
      return None

    if node.isTerminal():
      return Node.evaluatedValue(node, results)

    if node.value == "=":
      right = Node.evaluate(node.right, results)
      if (node.left is not None and
          node.left.isVariable() and
          right is not None):
        results[node.left.value] = right
      return None

    left = Node.evaluate(node.left, results)
    right = Node.evaluate(node.right, results)

    if left is None or right is None:
      return None

    if node.value == "+":
      return left + right

    if node.value == "-":
      return left - right

    if node.value == "*":
      return left * right

    if node.value == "/":
      if right == 0:
        return None
      return left / right


  @staticmethod
  def evaluatedValue(node, results):
    value = node.value

    if node.isVariable():
      if node.value not in results:
        return None
      value = results[node.value]

    return float(value)


  @staticmethod
  def copy(node):
    if node is None:
      return None

    newNode = Node(node.value)
    newNode.left = Node.copy(node.left)
    newNode.right = Node.copy(node.right)

    return newNode


  @staticmethod
  def replace(node, target, value):
    if node is target:
      return value

    if node.left is target:
      node.left = value
    if node.right is target:
      node.right = value

    return node


  @staticmethod
  def traverseInOrder(node):
    if node is None:
      return []

    return ([node] +
            Node.traverseInOrder(node.left) +
            Node.traverseInOrder(node.right))


  @staticmethod
  def toString(node):
    if node is None:
      return ""

    if node.isTerminal():
      return node.value

    return "({0} {1} {2})".format(node.value,
                                  Node.toString(node.left),
                                  Node.toString(node.right))
