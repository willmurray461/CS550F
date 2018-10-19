from PIL import Image
import math
import random

image1 = Image.new("RGB",(512, 512))

angle = 0
radius = 0

for x in range(0, 2560):
	angle += 1
	radius += 0.1
	image1.putpixel((math.floor(256 + radius*math.cos(math.radians(angle))), math.floor(256 + radius*math.sin(math.radians(angle)))), (255, 0, 0))

image2 = Image.new("RGB",(512, 512))

column = 0

row = 0

for z in range(0, 8):
	for x in range(0, 4):
		for x in range (0, 64):
			for y in range(0, 64):
				image2.putpixel((x + column, y + row), (255, 0, 0))
		column += 128
	row += 64
	if z%2 == 0:
		column = 64
	else:
		column = 0

image3 = Image.new("RGB", (512, 512))

for z in range(0,50):
	colorR = random.randrange(0,256)
	colorG = random.randrange(0,256)
	colorB = random.randrange(0,256)
	x = random.randrange(0,512)
	for y in range(0,512):
		image3.putpixel((x, y), (colorR, colorG, colorB))
		x += random.randrange(-3,4)
		if x >= 512:
			x = 511
		elif x < 0:
			x = 0

image4 = Image.new("RGB", (512, 512))

for z in range(0,50):
	colorR = random.randrange(0,256)
	colorG = random.randrange(0,256)
	colorB = random.randrange(0,256)
	x = random.randrange(0,512)
	for y in range(0,512):
		r = random.randrange(-3,4)
		for w in range(0, abs(r) + 1):
			if x + r >= 512:
				r = 511 - x
			elif x + r < 0:
				r = 0 - x
			if r > 0:
				image4.putpixel((x + r - w, y), (colorR, colorG, colorB))
			elif r < 0:
				image4.putpixel((x + r + w, y), (colorR, colorG, colorB))
			else:
				image4.putpixel((x, y), (colorR, colorG, colorB))
		x = x + r
		
def mandelbrot(sizex, sizey):
	mandelbrot = Image.new("RGB", (sizex, sizey))

	coords = [[] for x in range(0, sizey)]

	for x in range(0, sizey):
		coords[x] = [[] for y in range(0, sizex)]

	for x in range(0, sizey):
		for y in range(0, sizex):
			cx = -2 + ((4/(sizey - 1))*x)
			cy = -2 + ((4/(sizex - 1))*y)
			coordx = -2 + ((4/(sizey - 1))*x)
			coordy = -2 + ((4/(sizex - 1))*y)
			tempvar = 0
			escaped = False
			counter = 0
			while escaped == False and counter < 256:
				if math.sqrt(coordx**2 + coordy**2) >= 2:
					coords[x][y] = counter
					escaped = True
				else:
					tempvar = coordx
					coordx = coordx**2 - coordy**2 + cx
					coordy = 2*tempvar*coordy + cy
					counter += 1 
				if counter == 64:
					coords[x][y] = counter

	for x in range(0, sizey):
		for y in range(0, sizex):
			color = str(coords[x][y])
			color = int(color)
			mandelbrot.putpixel((x, y), (color, 0, 0))

	mandelbrot.save("demo_image.png", "PNG")

mandelbrot(2000,2000)







