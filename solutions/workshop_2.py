# 2020 Python Programming Workshop - Day 2: Snake
# Made possible by Engineering Service Learning and the Solar Energy Association

# Welcome to your second Python programming workshop! This is going to be a lot
# more exciting than the first workshop. You're going to be taking a very long
# learning leap going from workshop 1 to workshop 2, but hang in there!

# Prompt: create a game of "Snake" in python.
# These comments and some pre-written code will help you make your program.



# You don't need to worry about what this line of code does (for now). We will
# learn more about this in the future! Feel free to ignore it.

from lib.snake import *



# The "heading" is in what direction the snake is currently going. In this
# workshop, we have NORTH, EAST, SOUTH, and WEST. Define the heading that the
# player will start with.

heading = NORTH

# For this lab, we have a 50x50 canvas to work with. We need to give the snake
# a starting point. Add a cell to the snake to start off with.

add_snake_cell(24, 24)

# The game should loop forever. Can you remember how to loop forever?

while True:

	# Let's start off by getting the user's keystroke.

	key = get_keystroke()

	# Now that we've gotten the user's keystroke, we should think about what is
	# going to happen if we press UP, DOWN, LEFT, RIGHT, or ESCAPE. Can you
	# remember how we can execute instructions *if* something is True or False?

	if key == UP and heading != SOUTH:
		heading = NORTH
	elif key == DOWN and heading != NORTH:
		heading = SOUTH
	elif key == LEFT and heading != EAST:
		heading = WEST
	elif key == RIGHT and heading != WEST:
		heading = EAST

	# Let's put some food on the board now *if* there's no food on the board
	# already. If you want a challenge, try to make this happen so that the food
	# doesn't spawn on the snake either!

	while len(foods) < 1:
		if (newFoodPosition := (random_number(0, 49), random_number(0, 49))) not in cells:
			add_food_cell(newFoodPosition[0], newFoodPosition[1])

	# Now let's calculate the next position. This should be an ordered pair tuple
	# that adds the x and y of the head of the snake with the x and y of the
	# current heading. Hint: index -1 gives you the last item in a list.

	nextPosition = (cells[-1][0] + heading[0], cells[-1][1] + heading[1])

	# Let's calculate some lose conditions now. If the next position is off the
	# board, the player loses. If the next position is a coordinate that the snake
	# already resides at, the player loses because the snake will bite itself.

	if nextPosition[0] < 0 or nextPosition[0] > 49:
		lose_game()
	elif nextPosition[1] < 0 or nextPosition[1] > 49:
		lose_game()
	elif (nextPosition[0], nextPosition[1]) in cells:
		lose_game()

	# Assuming that we haven't lost at this point, this means that the next
	# position doesn't result in a lost game. Therefore, we should add that cell
	# to the cells that the snake lives on.

	add_snake_cell(nextPosition[0], nextPosition[1])

	# If the next position was a food cell, then the snake should not lose its the
	# tail cell, and the food should be removed. Otherwise, the snake should lose
	# the tail cell because this cancels out the cell addition we did before.

	if nextPosition in foods:
		remove_food_cell(nextPosition[0], nextPosition[1])
	else:
		remove_snake_cell(cells[0][0], cells[0][1])

	# Finally, let's show the display to the user.

	show_display()

# You did it! You made a snake game. Now run your program, fix some bugs, and
# have some fun with the game that you just made! 
