#imports random library
import random
#defines a funciton for simulating the "Monty Hall" problem
#when the contestant switches after a penny is revealed
def switch():
	#uses a global variable, wins, to record the amout of wins
	global wins
	#creates a list of doors
	doors = [0 for x in range(0,3)]
	#puts the car keys in one of the doors
	doors[random.randrange(0,3,1)] = 1
	#picks a random door
	r = random.randrange(0,3,1)
	#removes one of the doors with a penny that was not chose by the contestant.
	for x in range(0,3):
		if len(doors) == 3:
			if doors[x] == 0 and not x == r:
				doors.pop(x)
	#re-ajusts the contestant's selection with the door revealed
	if r == 0:
		r = 1
	else:
		r = 0
	#checks if the contestant won
	if doors[r] == 1:
		wins += 1
#defines a funciton for simulating the "Monty Hall" problem
#when the contestant doesn't switch after a penny is revealed
def noswitch():
	#uses a global variable, wins, to record the amout of wins
	global wins
	#creates a list of doors
	doors = [0 for x in range(0,3)]
	#puts the car keys in one of the doors
	doors[random.randrange(0,3,1)] = 1
	#picks a random door
	r = random.randrange(0,3,1)
	#checks if the contestant won
	if doors[r] == 1:
		wins += 1
#resets the wins
wins = 0
#runs the simulation with switching 1000 times
for x in range(0,1000):
	switch()
print("Wins with switching: "+str(wins)+"\nPercentage: "+str(wins/1000))
#resets the wins
wins = 0
#runs the simulation with switching 1000 times
for x in range(0,1000):
	noswitch()
print("Wins without switching: "+str(wins)+"\nPercentage: "+str(wins/1000))






