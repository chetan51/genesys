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


  def toString(self):
    return self.value

