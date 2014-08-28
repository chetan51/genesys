# Genesys: Evolving Programs to Solve Problems

## Architecture

	Node
		- value
		- isTerminal
		- left
		- right

	Program
		- root
		- fitness
		- run(assignments, maxTime=1000)
			- Returns: assignments, or None if maxTime is reached
		- mate(program)
			- Returns: program
		- print
			- Returns: string

	Population
		- programs
		- problem
		- init(n, problem)
		- computeFitnesses()
			- Returns: (min, max, average, standard deviation)
		- killWeakest(n)
		- mateStrongest(n)
		- mutate()
		- _createProgram(problem)
			- Returns: program
		- getBest()
			- Returns: program

	Problem (all static)
		- TERMINALS
		- OPERATORS
		- INPUTS
		- OUTPUTS
		- computeFitness(program)
			- Returns: int
