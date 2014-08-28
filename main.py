#! /usr/bin/env python

from classes.population import Population
from problems.fit_curve_problem import FitCurveProblem



def run():
  population = Population(FitCurveProblem)
  size = population.size

  for i in xrange(1, 101):
    print "========================================="
    print "Generation\t{0}".format(i)
    print "========================================="

    stats = population.computeFitnesses()
    print "-----------------------------------------"
    print "Stats:"
    print "-----------------------------------------"
    print stats

    best = population.getBest()
    print "-----------------------------------------"
    print "Best:"
    print "-----------------------------------------"
    print best.toString()

    population.killWeakest(size / 2)
    population.mateStrongest(size / 2)
    population.mutate()



if __name__ == "__main__":
  run()
