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
		- fitness
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
			- Returns: (min, max, average, standard deviation)
		- killWeakest(n)
		- mateStrongest(n)
		- mutate()
		- getBest()
			- Returns: program
		- _createProgram(problem) [static]
			- Returns: program

	AbstractProblem
		- TERMINALS [static]
		- OPERATORS [static]
		- INPUTS [static]
		- OUTPUTS [static]
		- init(args)
		- computeFitness(program)
			- Returns: int
