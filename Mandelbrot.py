#importing necessary libraries for math calculations and image generation
import math
from PIL import Image


#defines a function to generate a mandelbrot image
def mandelbrot(size, accuracy):
	#initializes a new blank RGB image with a resolution of size x size
	mandelbrot = Image.new("RGB", (size, size))
	#creates a one dimentional array which will hold the values for each pixel
	coords = [[] for x in range(0, size)]
	#adds another dimention to the aforementioned array, thus creating a 2D array of pixels
	for x in range(0, size):
		coords[x] = [[] for y in range(0, size)]
	#This function loops for each x,y value in the array and determines which shade of red each pixel will be
	for x in range(0, size):
		for y in range(0, size):
			#This variable represents the x component value of C
			cx = -2 + ((4)/(size - 1)*x)
			#This variable represents the y component value of C
			cy = -2 + ((4)/(size - 1)*y)
			#This represents the first (not zeroeth) x component value of Z
			zx = -2 + ((4/(size - 1))*x)
			#This represents the first (not zeroeth) y component value of Z
			zy = -2 + ((4/(size - 1))*y)
			#This is a temporary variable used for updating the value of zx and zy
			tempvar = 0
			#This is a variable to determine whether or not Z has escaped
			escaped = False
			#This is a counter to measure how many times the following while loop has run
			counter = 0
			#This while loop checks how many times it takes Z to escape, or if it doesn't after 256 attempts
			#Accuracy is how many shades of red the user wants to use 0-256
			while escaped == False and counter < accuracy:
				#This checks if Z has escaped
				if math.sqrt(zx**2 + zy**2) >= 2: 
					#This sets the shade of red of the pixel x,y depending on how many attempts it took to escape and the level of accuracy
					coords[x][y] = int(counter/accuracy * 255)
					#This tells the loop that the Z has escaped
					escaped = True
				#If Z has not escaped:
				else:
					#This uses 'tempvar' to store the value of zx
					tempvar = zx
					#This squares Z and adds C
					zx = zx**3 - zy**3 + cx
					zy = 3*tempvar*zy + cy
					#This increases the counter by 1
					counter += 1 
				#If Z has not escaped after 255 attempts:
				if counter == accuracy:
					#This sets the shade of red of the pixel x,y to solid red
					coords[x][y] = int(counter/accuracy * 255)

	#This function loops over for each pixel x,y
	for x in range(0, size):
		for y in range(0, size):
			#Converts the color value of each pixel in the pixel array to an integer
			color = str(coords[x][y])
			color = int(color)
			#Places the pixel on the image
			mandelbrot.putpixel((x, y), (color-50, color%2*x-50, color%256*y-50))

	#Saves the image
	mandelbrot.save("demo_image.png", "PNG")

#Calls the Mandelbrot function
mandelbrot(512, 256)
