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
		- init(size, problem)
		- computeFitnesses()
			- Returns: (min, max, average, standard deviation)
		- killWeakest(n)
		- mateStrongest(n)
		- mutate()
		- getBest()
			- Returns: program
		- _createProgram(problem) [static]
			- Returns: program

	AbstractProblem [all static]
		- TERMINALS
		- OPERATORS
		- INPUTS
		- OUTPUTS
		- computeFitness(program)
			- Returns: int
