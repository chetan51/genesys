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
		- getBest(fitnesses)
			- Returns: program
		- _createProgram(problem) [static]
			- Returns: program
		- fitnessStats(fitnesses)
			- Returns: (min, max, average, standard deviation)

	AbstractProblem
		- TERMINALS [static]
		- OPERATORS [static]
		- INPUTS [static]
		- OUTPUTS [static]
		- init(args)
		- computeFitness(program)
			- Returns: int
