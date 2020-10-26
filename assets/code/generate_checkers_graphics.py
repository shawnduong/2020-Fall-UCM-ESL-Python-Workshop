# This generates a checkerboard image. Some cool code to look at if you're
# interested in using Python for graphics. Pretty basic and easy to follow.

from PIL import Image, ImageDraw

# Size of the square image.
SIZE = 720

# Defining RGB values of some color constants.
WHITE  = (251, 238, 228)
GREEN  = (102, 204, 102)
RED    = (237,  67,  55)
YELLOW = (222, 244,  64)

def generate_checkerboard():
	"""
	This function generates the checkerboard graphic.
	"""

	# Create a new image object and a place to write pixels.
	img = Image.new("RGB", (SIZE, SIZE))
	pix = []

	# Write pixels in a checkerboard pattern.
	for x in range(SIZE):
		for y in range(SIZE):
			if x % (SIZE/4) < (SIZE/8) and y % (SIZE/4) < (SIZE/8):
				pix.append(WHITE)
			elif x % (SIZE/4) > (SIZE/8) and y % (SIZE/4) > (SIZE/8):
				pix.append(WHITE)
			else:
				pix.append(GREEN)

	# Write the pixels to the image and save it.
	img.putdata(pix)
	img.save("checkerboard.png")

def generate_piece(color):
	"""
	This function generates the graphics of a checker piece.
	"""

	# Calculate the size of a piece and create a new image.
	square = (SIZE/8)
	image  = Image.new("RGBA", (int(SIZE/8), int(SIZE/8)))

	if color == WHITE:
		name = "WHITE"
	elif color == RED:
		name = "RED"
	elif color == YELLOW:
		name = "YELLOW"

	# Draw a circle.
	draw = ImageDraw.Draw(image)
	draw.ellipse((5, 5, square-5, square-5), fill=color)

	# Save the image.
	image.save(f"piece_{name}.png", "PNG")

if __name__ == "__main__":
	generate_checkerboard()
	generate_piece(WHITE)
	generate_piece(RED)
	generate_piece(YELLOW)
