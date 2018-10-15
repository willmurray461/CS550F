from PIL import Image
import math

image = Image.new("RGB",(512, 512))

angle = 0
radius = 0

for x in range(0, 2560):
	angle += 1
	radius += 0.1
	image.putpixel((math.floor(256 + radius*math.cos(math.radians(angle))), math.floor(256 + radius*math.sin(math.radians(angle)))), (255, 0, 0))

image.save("demo_image.png", "PNG")