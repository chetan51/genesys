#! /usr/bin/env python

from classes.population import Population
from problems.fit_curve_problem import FitCurveProblem



NUM_GENERATIONS = 1000



def run():
  size = 100
  population = Population(FitCurveProblem, size=size)

  for i in xrange(1, NUM_GENERATIONS + 1):
    print "========================================="
    print "Generation:\t{0}".format(i)
    print "========================================="

    fitnesses = population.computeFitnesses()
    stats = population.computeFitnessStats(fitnesses)
    print "-----------------------------------------"
    print "Stats:"
    print "-----------------------------------------"
    print stats

    best = population.sortProgramsByFitness(fitnesses)[0]
    print "-----------------------------------------"
    print "Best:"
    print "-----------------------------------------"
    print best.toString()

    population.killWeakest(size / 2, fitnesses)
    population.mateStrongest(size / 2, fitnesses)
    population.mutate()



if __name__ == "__main__":
  run()
