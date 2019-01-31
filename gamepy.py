#imports the necessary libraries
import sys, math, random, pygame

#initiates pygame
pygame.init()
#sets the name of the window to "Pygame Asteroids Demo"
pygame.display.set_caption('Pygame Asteroids Demo')
#sets the size of the window to 640x480 and fills it in with black
screen = pygame.display.set_mode((640, 480))
screen.fill((0, 0, 0))
#defines colors which will be used later
white = (255, 255, 255)
black = (0, 0, 0)
#ship class
class ship:
	def __init__(self, pos):

		#declares used global variables
		global screen
		global white
		global black
		global torpedoes
		#declares local variables
		self.pos = pos
		self.speed = 0, 0
		self.angle = 0
		self.keys = [0, 0, 0, 0]
		self.reload = 0

	#defines the draw function, which draws the spaceship
	def draw(self):
		#calculates the three points of the triangle shaped spaceship using trigonometry
		a = (self.pos[0] + 10*math.cos(self.angle), self.pos[1] + 10*math.sin(self.angle))
		b = (self.pos[0] + 7*math.cos(self.angle + 2*math.pi/3), self.pos[1] + 7*math.sin(self.angle + 2*math.pi/3))
		c = (self.pos[0] + 7*math.cos(self.angle - 2*math.pi/3), self.pos[1] + 7*math.sin(self.angle - 2*math.pi/3))
		#creates a point list with the three points
		#vtcs stands for vertices
		self.vtcs = [a, b, c]
		#draws a triangle on the screen
		pygame.draw.polygon(screen, white, self.vtcs, 1)

	#defines the update function, which updates the position of the spaceship
	#and handles key presses
	def update(self):
		#checks for key presses
		key = pygame.key.get_pressed()

		if key[pygame.K_w]:
			if self.reload <= 0:
				#creates a new torpedo and fires it in the direction the ship is facing
				torpedo1 = torpedo((round(self.pos[0] + 10*math.cos(self.angle)), round(self.pos[1] + 10*math.sin(self.angle))), (4*math.cos(self.angle), 4*math.sin(self.angle)))
				#adds the torpedo to the list of torpedoes
				torpedoes.append(torpedo1)
				#adds to the reload time
				self.reload = 20
		#subtracts 1 from the reload counter
		#since the game runs at 30fps, this will take 2/3 seconds
		self.reload -= 1

		if key[pygame.K_a]:
			self.keys[0] = 1

		if key[pygame.K_s]:
			self.keys[1] = 1

		if key[pygame.K_d]:
			self.keys[2] = 1

		if self.keys[0] == 1:
			self.angle  -= 0.1

		if self.keys[2] == 1:
			self.angle  += 0.1

		if self.keys[1] == 1:
			#accelerates the ship
			self.speed = self.speed[0] + 0.05*math.cos(self.angle), self.speed[1] + 0.05*math.sin(self.angle)
			#creates a random flame particle (triangle) behind the spaceship
			#again, uses trigonometry same as drawing of the ship
			r = random.randrange(7, 15);

			d = (self.pos[0] + 7*math.cos(self.angle + 3*math.pi/4), self.pos[1] + 7*math.sin(self.angle + 3*math.pi/4))
			e = (self.pos[0] + r*math.cos(self.angle + math.pi), self.pos[1] + r*math.sin(self.angle + math.pi))
			f = (self.pos[0] + 7*math.cos(self.angle - 3*math.pi/4), self.pos[1] + 7*math.sin(self.angle - 3*math.pi/4))
			
			self.vtcs = [d, e, f]
			
			pygame.draw.polygon(screen, white, self.vtcs, 1)

		self.pos = self.pos[0] + self.speed[0], self.pos[1] + self.speed[1]

		#sets maximum speed
		if self.speed[0] > 3:
			self.speed = 3,self.speed[1]

		if self.speed[1] > 3:
			self.speed = self.speed[0],3

		if self.speed[0] < -3:
			self.speed = -3,self.speed[1]

		if self.speed[1] < -3:
			self.speed = self.speed[0],-3

		#warps the ship around the screen
		if self.pos[0] > 630:
			self.erase()
			self.pos = 10,self.pos[1]

		if self.pos[0] < 10:
			self.erase()
			self.pos = 630,self.pos[1]

		if self.pos[1] > 470:
			self.erase()
			self.pos = self.pos[0],10

		if self.pos[1] < 0:
			self.erase()
			self.pos = self.pos[0],470
		
		#resets the key presses
		key = pygame.key.get_pressed()

		if not key[pygame.K_a]:
			self.keys[0] = 0

		if not key[pygame.K_s]:
			self.keys[1] = 0

		if not key[pygame.K_d]:
			self.keys[2] = 0

	#defines the function for erasing the ship
	def erase(self):
		a = (self.pos[0] + 25*math.cos(self.angle), self.pos[1] + 25*math.sin(self.angle))
		b = (self.pos[0] + 25*math.cos(self.angle + 2*math.pi/3), self.pos[1] + 25*math.sin(self.angle + 2*math.pi/3))
		c = (self.pos[0] + 25*math.cos(self.angle - 2*math.pi/3), self.pos[1] + 25*math.sin(self.angle - 2*math.pi/3))
		
		self.vtcs = [a, b, c]
		#same as draw function, but uses black to rease the ship and a larger triangle
		# to make sure all particles are erased too
		pygame.draw.polygon(screen, black, self.vtcs, 100)
#asteroid class
class asteroid:
	def __init__(self, pos, size):
		#again, declares global & vars local
		global screen
		global white
		global black

		self.size = size
		self.pos = pos
		#generates a random speed for the asteroid
		#smaller asteroids move faster
		self.speed = random.randint(-1,2)*random.random()*2/size, random.randint(-1,2)*random.random()*2/size
		self.rands = []
		self.vtcs = [0 for x in range(0,12)]
		#creates a randomly shaped "circular" ploygon with 12 points
		#this is done by placing twelve points at equally spaced angles with different 
		#distances from the center
		#the resulting distances are stored in "rands"
		for x in range(0,12):
			r = random.randrange(self.size*5, self.size*9)
			self.rands.append(r)
		
	def draw(self):
		
		#this function generates the 12 points based on the distances stored in rands
		#using, again, trigonometry and puts them in the list
		for x in range(0,12):
			p = (self.pos[0] + self.rands[x]*math.cos(x*math.pi/6), self.pos[1] + self.rands[x]*math.sin(x*math.pi/6))
			self.vtcs[x] = p
		#draws the asteroid
		pygame.draw.polygon(screen, white, self.vtcs, 1)

	def update(self):
		
		#moves the asteriod
		self.pos = self.pos[0] + self.speed[0], self.pos[1] + self.speed[1]

		#warps the asteriod across the edges of the screen
		if self.pos[0] > 650:
			self.erase()
			self.pos = -10,self.pos[1]

		if self.pos[0] < -10:
			self.erase()
			self.pos = 650,self.pos[1]

		if self.pos[1] > 490:
			self.erase()
			self.pos = self.pos[0],-10

		if self.pos[1] < -10:
			self.erase()
			self.pos = self.pos[0],490

	#same as draw, but with black as color for erasing and larger thickness to ensure 
	#the whole asteroid is erased
	def erase(self):

		for x in range(0,12):
			p = (self.pos[0] + self.rands[x]*math.cos(x*math.pi/6), self.pos[1] + self.rands[x]*math.sin(x*math.pi/6))
			self.vtcs[x] = p

		pygame.draw.polygon(screen, black, self.vtcs, 2)

#torpedo class
class torpedo():
	def __init__(self, pos, speed):
		#same stucc
		global screen
		global white
		global black

		self.pos = pos
		self.speed = speed

	#draws a simple circle, erases, then moves, the draws it.
	def draw(self):
		pygame.draw.circle(screen, white, self.pos, 2, 2)

	def update(self):
		self.pos = int(self.pos[0] + self.speed[0]), int(self.pos[1] + self.speed[1])

	def erase(self):
		pygame.draw.circle(screen, black, self.pos, 2, 2)

#creates a new ship
ship1 = ship((320, 240))
#creates a list of asteroids and torpedoes
asteroids = []
torpedoes = []

#generates asteroids at random positions
for x in range(0,2):
	x = asteroid((random.randrange(50, 200), random.randrange(50, 100)), 3)
	y = asteroid((random.randrange(390, 590), random.randrange(330, 430)), 3)
	asteroids.append(x)
	asteroids.append(y)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

#runs all of the ship code
	ship1.erase()
	ship1.update()
	ship1.draw()

#runs all of the asteroid code for all of the asteroids
	for x in asteroids:
		x.erase()
		x.update()
		x.draw()
#runs all of the torpedo code for all of the torpedo
	for x in torpedoes:
		x.erase()
		x.update()
		x.draw()
#collision detection for asteroids and torpedoes
	for x in asteroids:
		for y in torpedoes:
			#this is done by measuring the distance between their centers and factoring
			#the size of the asteroid into the equation
			#essentially, this uses circular hitboxes
			if math.sqrt((x.pos[0]-y.pos[0])**2 + (x.pos[1]-y.pos[1])**2) < x.size*8:
				#erases the torpedo and asteroid, and removes them from their respective lists
				#thus, they will no longer be updated
				x.erase()
				asteroids.remove(x)
				y.erase()
				torpedoes.remove(y)
				#generates new, smaller asteroids when a bigger one splits after being hit
				if x.size == 3:
					for z in range(0,2):
						asteroids.append(asteroid(x.pos,x.size-1))
				if x.size == 2:
					for z in range(0,3):
						asteroids.append(asteroid(x.pos,x.size-1))
#hit detection for ships and asteriods	
	for x in asteroids:
		if math.sqrt((x.pos[0]-ship1.pos[0])**2 + (x.pos[1]-ship1.pos[1])**2) < x.size*8 + 10:
			#if the ship is hit, move it back to the center
			ship1.erase()
			ship1.speed = (0, 0)
			ship1.pos = (320, 240)
			#as you might have been able to tell, there are infinite lives in this game
			#i did this because I'm not very good at it and is kind of frustrating
#creates new asteroids if all the old ones are destroyed in the same way that
#the initial ones are generated			
	if len(asteroids) <= 0:
		for x in range(0,2):
			x = asteroid((random.randrange(50, 200), random.randrange(50, 100)), 3)
			y = asteroid((random.randrange(390, 590), random.randrange(330, 430)), 3)
			asteroids.append(x)
			asteroids.append(y)

#advance the display one frame
	pygame.display.flip()



