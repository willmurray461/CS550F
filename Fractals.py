#Imports the necessary library for image generation
from PIL import Image
#Imports a library for color modificaiton purposes
import colorsys
#Imports a library used to help with text output
import sys

#Defines a function which will draw Fractal #1 (Mandelbrot)
#Resolution is the number of pixels in both the horizontal and vertical directions
#e.g a resolution of 512 will create a 512x512 image.
#x1,y1 is the top left corner of the image, and can be used to shift the camera
#size is the width and height of the image, and can be used to zoom
#e.g an image with x1 of -1, y1 of -1, and size of 0.1 would look from (1,1) to (-0.9,-0.9)
def fractal_1(resolution,x1,y1,size):
	#Prints a part of a progress bar, indicating that the program is working to draw Fractal #1
	print("Drawing Fractal #1\n")
	#Initializes a new image in the RGB colorspace named fractal1
	fractal1 = Image.new("RGB",(resolution,resolution))
	#Creates a new complex number z with value 0 + 0i
	z = complex(0,0)
	#Creates a new counter variable, and set it to zero
	counter = 0
	#Creates a loop that will run once for each pixel in the image's horizontal resolution
	for x in range(0,resolution):
		#Calculates how much of the Fractal has been drawn by the program, which is used in the progress indicator
		completion = int(x/resolution*100)
		#Moves the cursor up one line
		sys.stdout.write("\033[F")
		#Prints the percentage of completion for the Fractal.
		print(completion,"\b% Complete...")
		#Creates a loop that will run once for each pixel in the image's vertical resolution
		for y in range(0,resolution):
			#Sets C to the currently selected pixel. C will loop through every pixel on the screen once
			c = complex(x1+size/(resolution-1)*x,y1+size/(resolution-1)*y)
			#Tests whether or not z has escaped
			if abs(z) >= 2 or counter >= 256:
				#Puts a pixel on the screen, with color depending on how many attempts it took to escape
				#Gradient colors are also implemented due to modification in the numbers below
				fractal1.putpixel((x,y),(counter-50,counter%2*x-50,counter%256*y-50))
				#Resets Z to zero
				z = complex(0,0)
				#Resets counter to zero
				counter = 0
			#Does this if Z has not escaped
			else:
				#Creates the next iteration of Z
				z = z**2+c
				#Increases the counter by 1
				counter+=1
	#Saves the Image as "demo_image1.png"
	fractal1.save("demo_image1.png","PNG")
#Calls the Fractal1 function with pre-selected values
#fractal_1 creates a cool effect by making the image look corrupted by not utilizing a while loop
#to check if Z has escaped. This way, every pixel is only tested once. 
#however the counter variable and iterations of Z still carry on between pixels as they are not reset
#unless the funciton escapes and draws a pixel. The function, I guess, "approximates" the mandelbrot
#set, and because it only tests each pixel once, it is very fast.
fractal_1(512,-2,-1.75,2)

#Defines a function to draw Fractal 2 (Mandelbrot). It takes the same inputs and the previous fractal function
def fractal_2(resolution,x1,y1,size):
	#Prints a part of a progress bar, indicating that the program is working to draw Fractal #1
	print("Drawing Fractal #2\n")
	#Initializes a new image in the RGB colorspace named fractal2
	fractal2 = Image.new("RGB",(resolution,resolution))
	#Creates a new complex number z with value 0 + 0i
	z = complex(0,0)
	#Creates a new counter variable, and set it to zero
	counter = 0
	#Creates a loop that will run once for each pixel in the image's vertical resolution
	for x in range(0,resolution):
		#Calculates how much of the Fractal has been drawn by the program, which is used in the progress indicator
		completion = int(x/resolution*100)
		#Moves the cursor up one line
		sys.stdout.write("\033[F")
		#Prints the percentage of completion for the Fractal.
		print(completion,"\b% Complete...")
		#Creates a loop that will run once for each pixel in the image's vertical resolution
		for y in range(0,resolution):
			#Sets C to the currently selected pixel. C will loop through every pixel on the screen once
			c = complex(x1+size/(resolution-1)*x,y1+size/(resolution-1)*y)
			#Creates a boolean to indicate to the program if Z has escaed yet, and sets it to false
			escaped = False
			#Loops over while Z has not escaped yet
			while escaped == False:
				#Tests whether or not z has escaped
				if abs(z) >= 2 or counter >= 256:
					#Puts a pixel on the screen, with color depending on how many attempts it took to escape
					#This program also takes the color input as HLS, and converts it to RGB, this achieves
					#a sort of glowing effect that looks nice
					color = colorsys.hls_to_rgb(counter,counter,counter)
					fractal2.putpixel((x,y),(int(color[0]),int(color[1]),int(color[2])))
					#Resets Z to zero
					z = complex(0,0)
					#Resets counter to zero
					counter = 0
					#Tells the loop that Z has escaped, and ends it
					escaped = True
				#Does this if Z has not escaped
				else:
					#Creates the next iteration of Z
					z = z**2+c
					#Increases the counter by 1
					counter+=1
	#Saves the Image as "demo_image1.png"
	fractal2.save("demo_image2.png","PNG")
#Calls the fractal_2 function with pre-selected values
fractal_2(500,-0.2466,-1.1416,0.26)

#Defines a function to draw Fractal 3 (Julia). It takes the same inputs and the previous fractal functions
def fractal_3(resolution,x1,y1,size):
	#Prints a part of a progress bar, indicating that the program is working to draw Fractal #1
	print("Drawing Fractal #3\n")
	#Initializes a new image in the RGB colorspace named fractal3
	fractal3 = Image.new("RGB",(resolution,resolution))
	#Creates a new complex number z with value 0 + 0i
	counter = 0
	#Creates a loop that will run once for each pixel in the image's vertical resolution
	for x in range(0,resolution):
		#Calculates how much of the Fractal has been drawn by the program, which is used in the progress indicator
		completion = int(x/resolution*100)
		#Moves the cursor up one line
		sys.stdout.write("\033[F")
		#Prints the percentage of completion for the Fractal.
		print(completion,"\b% Complete...")
		#Creates a loop that will run once for each pixel in the image's vertical resolution
		for y in range(0,resolution):
			#Sets the intial value of Z to the currently selected pixel. Z will loop through every pixel on the screen once
			z = complex(x1+size/(resolution-1)*x,y1+size/(resolution-1)*y)
			#Creates a boolean to indicate to the program if Z has escaed yet, and sets it to false
			escaped = False
			#Loops over while Z has not escaped yet
			while escaped == False:
				#Tests whether or not z has escaped
				if abs(z) >= 2 or counter >= 256:
					#Puts a pixel on the screen, with color depending on how many attempts it took to escape
					#This program also takes the color input as HLS, and converts it to RGB, this achieves
					#an image with nice contrast between two colors: red and blue
					color = colorsys.hls_to_rgb(counter-128,counter-128,counter-128)
					fractal3.putpixel((x,y),(int(color[0]),int(color[1]),int(color[2])))
					#Resets Z to zero
					z = complex(0,0)
					#Resets counter to zero
					counter = 0
					#Tells the loop that Z has escaped, and ends it
					escaped = True
				#Does this if Z has not escaped
				else:
					#Creates the next iteration of Z
					z = z**2-0.7269+0.1889j
					#Increases the counter by 1
					counter+=1
	#Saves the Image as "demo_image1.png"
	fractal3.save("demo_image3.png","PNG")
#Calls the fractal_3 function with pre-selected values
fractal_3(512,-0.25,-0.25,0.5)