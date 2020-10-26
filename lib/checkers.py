# 2020 Python Programming Workshop - Day 3: Checkers
# Made possible by Engineering Service Learning and the Solar Energy Association

# Welcome to your third Python programming workshop! This is going to be a lot
# different than any other one that we've done before.

# Prompt: create a game of "Checkers" in python.
# These comments and some pre-written code will help you make your program.

# These are imports. They bring libraries into our program.

import pygame
import sys

# Initialize the pygame library.

pygame.init()

# Define some color constants.

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

class Checkers:
	"""
	This is a class for a game of checkers.
	"""

	# Some attributes (that's an important vocabulary word).

	display = None
	board   = None
	pieces  = None
	clock   = None
	refresh = None

	# More attributes but for the game.
	selected = None
	moved    = False
	turn     = 0

	def __init__(self):
		"""
		Constructor method. This is the method that is first called upon
		instantiation (fancy way of saying creating, i.e. create an instance of).
		"""

		# Set the attributes.

		self.display = pygame.display.set_mode((720, 720))
		self.board   = Checkerboard()
		self.refresh = 60
		self.clock   = pygame.time.Clock()

		# Create and store the pieces in the game.

		self.pieces = {}

		# 3 ranks, 8 files, place pieces on checkered tiles only.
		# This code might seem sinister, but break it down slowly and you'll see.
		for x in range(8):
			for y in range(3):
				if (x+y) % 2 == 1:
					coordinates = (x, y)
					self.pieces[coordinates] = Checkerpiece("red")
					# * means "splat" or "expand"... so (x, y) becomes x, y.
					self.pieces[coordinates].place(coordinates)
					self.pieces[(7-coordinates[0], 7-coordinates[1])] = Checkerpiece("white")
					self.pieces[(7-coordinates[0], 7-coordinates[1])].place((7-coordinates[0], 7-coordinates[1]))
				else:
					# If the current tile is not checkered, skip over it.
					pass

	def play(self):
		"""
		The main game loop itself.
		"""

		# Variables for the piece selected and the turn counter.

		self.selected = None
		self.turn     = 0

		# Infinite loop.

		while True:

			# Calculate whose turn it is.

			if self.turn % 2 == 0:
				color = "white"
			else:
				color = "red"

			# Handle events.

			for event in pygame.event.get():

				# If the user is pressing ESCAPE, exit the game.

				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					sys.exit(0)

				# If the user is clicking their mouse... (this is where you start coding!)

				elif event.type == pygame.MOUSEBUTTONDOWN:

					########## Your code starts here. ##########
					# Remember to consult the manual for help! #
					############################################

					# We need to find out which tile the user clicked... we need to get the coordinates.



					# If the player selected their own non-highlighted piece...
					# (Remember to give valid inputs, see the manual!)



						# The current piece is the piece at the coordinate.

						piece = self.pieces[coordinates] # Here's a freebie.

						# Set self.selected to a copy of the selected piece.



						# Highlight the selected piece.
						# (Remember to give valid inputs, see the manual!)



					# If the player selected their own highted piece...
					# (Remember to give valid inputs, see the manual!)



						# Unhighlight the piece.



					# Otherwise if a piece is highlighted and the player selects another tile...



						# If a piece move is successful...



							# Increment turns by 1.



					################ Your code ends here. ######################
					# Good job! You're all done. You should run your code now. #
					############################################################

			# Show the display.

			self.show_display()

	# All code below this line is fancy support stuff. Read on if you'd like to
	# satisfy your own curiosity! This is way more advanced so beware!

	def show_display(self):
		"""
		Show the display.
		"""

		self.board.draw(self.display)

		for coordinate in self.pieces.keys():
			self.pieces[coordinate].draw(self.display)

		pygame.display.update()
		self.clock.tick(self.refresh)

	def move_highlighted_piece_to_was_successful(self, coordinates):
		"""
		Move the highlighted piece to the specific coordinate. Return True if successful.
		"""

		x, y = coordinates[0], coordinates[1]

		self.moved = False

		if self.selected.color == "red":

			if coordinates == (self.selected.x+1, self.selected.y+1):
				self.moved = self.pieces.pop((x-1, y-1))
			elif coordinates == (self.selected.x-1, self.selected.y+1):
				self.moved = self.pieces.pop((x+1, y-1))

			elif coordinates == (self.selected.x+2, self.selected.y+2) and self.pieces[(x-1, y-1)].color == "white" and coordinates not in self.pieces.keys():
				self.moved = self.pieces.pop((x-2, y-2))
				self.pieces.pop((x-1, y-1))
			elif coordinates == (self.selected.x-2, self.selected.y+2) and self.pieces[(x+1, y-1)].color == "white" and coordinates not in self.pieces.keys():
				self.moved = self.pieces.pop((x+2, y-2))
				self.pieces.pop((x+1, y-1))

		elif self.selected.color == "white":

			if coordinates == (self.selected.x-1, self.selected.y-1):
				self.moved = self.pieces.pop((x+1, y+1))
			elif coordinates == (self.selected.x+1, self.selected.y-1):
				self.moved = self.pieces.pop((x-1, y+1))

			elif coordinates == (self.selected.x+2, self.selected.y-2) and self.pieces[(x-1, y+1)].color == "red" and coordinates not in self.pieces.keys():
				self.moved = self.pieces.pop((x-2, y+2))
				self.pieces.pop((x-1, y+1))
			elif coordinates == (self.selected.x-2, self.selected.y-2) and self.pieces[(x+1, y+1)].color == "red" and coordinates not in self.pieces.keys():
				self.moved = self.pieces.pop((x+2, y+2))
				self.pieces.pop((x+1, y+1))

		if self.moved != False:
			self.pieces[coordinates] = self.selected
			self.pieces[coordinates].place(coordinates)
			self.selected = None
			self.moved = False
			return True
		else:
			return False

	def piece_highlighted_and_player_selects_another_tile(self, color, coordinates):
		"""
		Returns True if, well, a piece is highlighted and the player selects another tile.
		"""

		x, y = coordinates[0], coordinates[1]

		if (x, y) not in self.pieces.keys() and self.selected != None:
			return True
		else:
			return False

	def unhighlight_selected(self, coordinates):
		"""
		Unhighlight the piece at the selected coordinates.
		"""

		self.pieces[coordinates] = self.selected
		self.selected = None

	def player_selected_their_own_highlighted_piece(self, color, coordinates):
		"""
		Return True if the selected (x, y) is a valid piece belonging to the player.
		"""

		x, y = coordinates[0], coordinates[1]

		if (x, y) in self.pieces.keys() and self.selected != None and self.selected.color == color and self.pieces[(x, y)].color == "yellow":
			return True
		else:
			return False

	def highlight_selected(self, coordinates):
		"""
		Highlight the piece at the selected coordinates.
		"""

		self.pieces[coordinates] = Checkerpiece("yellow", *coordinates)

	def selected_piece(self, piece):
		"""
		Return a copy of the selected piece.
		"""

		return Checkerpiece(piece.color, piece.x, piece.y)

	def player_selected_their_own_piece(self, color, coordinates):
		"""
		Return True if the selected (x, y) is a valid piece belonging to the player.
		"""

		x, y = coordinates[0], coordinates[1]

		if (x, y) in self.pieces.keys() and self.pieces[(x, y)].color == color:
			return True
		else:
			return False

	def get_coordinates(self, event):
		"""
		Translate a MOUSEBUTTONDOWN event into a coordinate click where:
		0 <= x < 8 and 0 <= y < 8 so that x,y will be a coordinate on our board.
		"""

		return event.pos[0] // 90, event.pos[1] // 90

class Checkerboard:
	"""
	This is a class for the checkerboard itself.
	"""

	# Attributes.

	image = None

	def __init__(self):
		"""
		Constructor method.
		"""

		# Upon instantiation, load up the checkerboard graphic.
		self.image = pygame.image.load("./assets/img/checkerboard.png")

	def draw(self, display):
		"""
		Method to draw the board.
		"""

		display.fill(BLACK)
		display.blit(self.image, self.image.get_rect())

class Checkerpiece:
	"""
	This is a class for a single checkerpiece.
	"""

	# Attributes

	image   = None
	color   = None
	heading = None

	x = None
	y = None

	def __init__(self, color, x=0, y=0):
		"""
		Constructor method. Takes a color and (optional) coordinates.
		"""

		# Load up graphics if the constructor was called correctly.

		if color not in ["red", "white", "yellow"]:
			print("Hey programmer, you tried selecting an invalid color that isn't valid!")
			print("This object can only be \"red\", \"white\", or \"yellow\". Remember that")
			print("Python and almost all programming language are case sensitive!")
			sys.exit(-1)
		elif color == "red":
			self.image = pygame.image.load("./assets/img/piece_RED.png")
		elif color == "white":
			self.image = pygame.image.load("./assets/img/piece_WHITE.png")
		else:
			self.image = pygame.image.load("./assets/img/piece_YELLOW.png")

		# Set the color.

		self.color = color

		# Set the coordinates.

		self.x = x
		self.y = y

	def place(self, coordinates):
		"""
		Place the piece at a new x, y coordinate.
		"""

		self.x, self.y = coordinates[0], coordinates[1]

	def draw(self, display):
		"""
		Draw the piece.
		"""

		display.blit(self.image, (self.x*90, self.y*90))

