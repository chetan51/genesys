class Program(object):


  def __init__(self, root):
    self.root = root
    self.fitness = 0


  def run(self, assignments, maxOperations=1000, maxTime=1000):
    raise NotImplementedError()


  def mate(self, program):
    raise NotImplementedError()


  def toString(self):
    raise NotImplementedError()
