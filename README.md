# Genesys: Evolving Programs to Solve Problems

## Architecture

	Node
		- value
		- isTerminal
		- left
		- right
		- setLeft(node)
		- setRight(node)

	Program
		- root
		- run(assignments, maxOperations=1000, maxTime=1000)
			- Returns: assignments, or None if maxOperations or maxTime is reached
		- mate(program)
			- Returns: program
		- toString()
			- Returns: string

	Population
		- programs
		- problem
		- init(problem, size=100)
		- computeFitnesses()
			- Returns: fitnesses (dict)
		- killWeakest(n, fitnesses)
		- mateStrongest(n, fitnesses)
		- mutate()
		- sortProgramsByFitness(fitnesses)
			- Returns: program
		- _createProgram(problem) [static]
			- Returns: program
		- computeFitnessStats(fitnesses)
			- Returns: (min, max, average, standard deviation)

	AbstractProblem
		- INPUTS [static]
		- OUTPUTS [static]
		- OPERATORS [static]
		- CONSTANTS [static]
		- init(args)
		- computeFitness(program)
			- Returns: int

# TODO

    - Clean up static vs instance methods in Node
    - Have Population call methods on Program to do mutation and random
    initialization instead of doing it itself
    - Clean up 1D regression problem

