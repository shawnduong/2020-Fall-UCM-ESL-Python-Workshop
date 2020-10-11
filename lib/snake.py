# 'pygame' is a library that helsp programmers create video games. We want to
# use its functionalities, so we can include it in the project by importing it.

import pygame

# This initializes the pygame library.

pygame.init()

# The game clock controls time passage based on the framerate.

gameClock = pygame.time.Clock()
FRAMERATE = 15

# The display is the window in which the game resides. This code creates a
# 500x500 resolution display for the player to interact with.

display = pygame.display.set_mode((500, 500))

# Here are some definitions to make the project easier for attendees.

UP     = pygame.K_UP
DOWN   = pygame.K_DOWN
LEFT   = pygame.K_LEFT
RIGHT  = pygame.K_RIGHT
ESCAPE = pygame.K_ESCAPE

BLACK  = pygame.Color(000, 000, 000)
WHITE  = pygame.Color(255, 255, 255)
RED    = pygame.Color(255, 000, 000)

NORTH  = ( 0, -1)
EAST   = (+1,  0)
SOUTH  = ( 0, +1)
WEST   = (-1,  0)

# This is some data related to the game's actors.

cells = [] # A list of ordered pairs denoting cells the snake resides on.
foods = [] # A list of ordered pairs denoting cells the foods reside on.

# Here are some custom functions related to the workshop that attendees can use.

def add_snake_cell(x, y):
	"""
	Add a new snake cell at (x, y).
	"""

	# Add a tuple (x, y) to the list cells.

	global cells
	cells.append((x, y))

def remove_snake_cell(x, y):
	"""
	Remove a snake cell at (x, y).
	"""

	import sys

	# Remove the tuple (x, y) from the list cells.

	global cells

	try:
		cells.remove((x, y))
	except:
		print("remove_snake_cell: Psst! You're trying to remove a cell that doesn't exist.")
		print("Review your program's logic and fix the bug, and then try again.")
		sys.exit(-1)

def remove_all_snake_cells():
	"""
	Remove all the snake cells.
	"""

	# Clear the list cells.

	global cells
	cells = []

def add_food_cell(x, y):
	"""
	Add a new food cell at (x, y).
	"""

	# Add the tuple (x, y) to the list foods.

	global foods
	foods.append((x, y))

def remove_food_cell(x, y):
	"""
	Remove a food cell at (x, y).
	"""

	# Remove the tuple (x, y) from the list foods.

	import sys

	global foods

	try:
		foods.remove((x, y))
	except:
		print("remove_food_cell: Psst! You're trying to remove a cell that doesn't exist.")
		print("Review your program's logic and fix the bug, and then try again.")
		sys.exit(-1)

def remove_all_food_cells():
	"""
	Remove all food cells.
	"""

	# Clear the list foods.

	global foods
	foods = []

def wait(seconds):
	"""
	Wait for some amount of seconds.
	"""

	import time

	# Sleep for some number of seconds.
	time.sleep(seconds)

def show_display():
	"""
	Show the display to the player.
	"""

	display.fill(BLACK)       # Fill the display in with the background color.

	for cell in cells:        # Draw the snake.
		pygame.draw.rect(     # Draw a rectangle.
			display,          # Draw on the display.
			WHITE,            # Make the rectangle white.
			pygame.Rect(      # Define the rectangle with:
				1+cell[0]*10, # x coordinate start.
				1+cell[1]*10, # y coordinate start.
				8,            # Rectangle width.
				8,            # Rectangle height.
			),
		)

	for cell in foods:        # Draw the foods.
		pygame.draw.rect(     # Draw a rectangle.
			display,          # Draw on the display.
			RED,              # Make the rectangle red.
			pygame.Rect(      # Define the rectangle with:
				1+cell[0]*10, # x coordinate start.
				1+cell[1]*10, # y coordinate start.
				8,            # Rectangle width.
				8,            # Rectangle height.
			),
		)

	pygame.display.update()   # Update the display.
	gameClock.tick(FRAMERATE) # Move time forward based on the framerate.

def get_keystroke():
	"""
	Get the key pressed by the user.
	"""

	import pygame

	for event in pygame.event.get():           # Get the events going on.
		if event.type == pygame.KEYDOWN:       # Conditional for if the event is a keystroke.
			if event.key == pygame.K_UP:       # Keystroke: arrow up.
				return UP                      # Return UP.
			elif event.key == pygame.K_DOWN:   # Keystroke: arrow down.
				return DOWN                    # Return DOWN.
			elif event.key == pygame.K_LEFT:   # Keystroke: arrow left.
				return LEFT                    # Return LEFT.
			elif event.key == pygame.K_RIGHT:  # Keystroke: arrow right.
				return RIGHT                   # Return RIGHT.
			elif event.key == pygame.K_ESCAPE: # Keystroke: arrow escape.
				return ESCAPE                  # Return ESCAPE.
			else:                              # Else case (keystroke wasn't an arrow or escape).
				pass                           # Do nothing.
		else:                                  # Else case (event wasn't a keystroke).
			pass                               # Do nothing.

def lose_game():
	"""
	Lose the game.
	"""

	import sys
	import time

	# Draw white pixels from the bottom up.
	for y in range(50):
		for x in range(50):
			pygame.draw.rect(
				display,
				WHITE,
				pygame.Rect(
					1+x*10,
					1+y*10,
					8,
					8,
				),
			)
		time.sleep(0.01)        # Sleep for 0.01 seconds.
		pygame.display.update() # Update the display.

	sys.exit(0)   # Exit with code 0.

def quit_game():
	"""
	Quit the game.
	"""

	import sys

	# Exit with code 0 (OK code).
	sys.exit(0)

def random_number(a, b):
	"""
	Generate a random number between [a, b].
	"""

	import random

	# Return a random number.
	return random.randint(a, b)

