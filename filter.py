from PIL import Image
from PIL import ImageEnhance
import sys

image = Image.open(sys.argv[1])
image2 = Image.open("/Users/williammurray/Desktop/CS550F/cage.jpg")
xsize,ysize = image.size
image2 = image2.resize((xsize,ysize))
for x in range(0,ysize,2):
	part = image2.crop((0,x,xsize,x+1))
	image.paste(part,(0,x,xsize,x+1))

image.save("filtered_image.png","PNG")