from PIL import Image
import sys

image = Image.open(sys.argv[1])
image2 = Image.open("/Users/williammurray/Desktop/CS550F/cage.jpg")
xsize,ysize = image.size
image = image.rotate(30)
r,g,b = image.split()
image = Image.merge("RGB",(b,r,g))

def roll(image, delta):
    """Roll an image sideways."""
    xsize, ysize = image.size

    delta = int(delta*xsize/100)
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image

image = roll(image, 50)
image2 = image2.resize((xsize,ysize))

for x in range(0,ysize,2):
	part = image2.crop((0,x,xsize,x+1))
	image.paste(part,(0,x,xsize,x+1))

image.save("filtered_image.png","PNG")