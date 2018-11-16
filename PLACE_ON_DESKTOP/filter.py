# Imports necessary image manipulation and creation libraries
from PIL import Image
from PIL import ImageEnhance

# Imports sys to be able to recieve command line imput
import sys

# Takes in the user's image from the command line
try:
	image = Image.open(sys.argv[1])

# If the user incorrectly entered the location of their image,
# the program will tell the user and quit
except FileNotFoundError:
	print("Could not find an image at:\n\""+sys.argv[1]+"\"\nMake sure you entered the location of your image correctly.")
	sys.exit()

image2 = Image.open(var)

# Loads asset from folder
# For some reason it won't work if I write '~/Desktop/PLACE_ON_DESKTOP/cage.jpg',
# so the the code might need to be edited if used on another computer.
try:
	image2 = Image.open("/Users/williammurray/Desktop/PLACE_ON_DESKTOP/cage.jpg")

# If the program cannot load the asset, it will tell the user and quit
except FileNotFoundError:
	print("Asset missing/failed to load. Make sure you downloaded the entire folder:\n'PLACE_ON_DESKTOP'\nand placed it on your desktop.")
	sys.exit()

# Sets two variables for the height and width of the image
xsize,ysize = image.size

# Resizes the asset to match the size of the user's image
image2 = image2.resize((xsize,ysize))

# Individually cuts every other line from the asset and pastes it on the user's image
for x in range(0,ysize,2):
	part = image2.crop((0,x,xsize,x+1))
	image.paste(part,(0,x,xsize,x+1))

# Saves the modified image
image.save("filtered_image.jpg","JPEG")