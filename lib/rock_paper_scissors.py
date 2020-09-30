def computer_choice() -> str:
	"""
	This function takes no inputs and returns either "rock", "paper", or
	"scissors" randomly to simulate the computer's decision.
	"""

	# 'random' is a library. A library is essentially a collection of code that
	# contains some kind of feature(s) that we want to use in our program. In
	# order to use these features, we need to bring the library into our program.
	# This is what is meant by 'importing' a library.

	import random

	# A function can 'return' a value, allowing it to directly represent some kind
	# of data. In this case, we are returning the output of the choice function
	# (from the random library). This choice function has 1 input (argument): a
	# tuple of 3 possible comma-separated choices that it may return.

	return random.choice( ("rock", "paper", "scissors") )

