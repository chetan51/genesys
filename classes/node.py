class Node(object):


  def __init__(self, value, isTerminal):
    self.value = value
    self.isTerminal = isTerminal
    self.left = None
    self.right = None


  def setLeft(self, node):
    self.left = node


  def setRight(self, node):
    self.right = node
