import random
import math
import matplotlib.pyplot as plt


# results = []
# for j in range(1000):
# 	total = 0
# 	for i in range(10):
# 		flip = random.randint(0,1)
# 		total += flip
# 	results.append(total)

# display = [0 for i in range(11)]
# for i in range(len(results)):
# 	display[results[i]] += 1

# r = [x for x in range(11)]

# #plt.plot(r,display,'gs')
# plt.bar(r,display,color=(0.5,1.0,0.5,0.5))
# plt.ylabel("Number of Trials")
# plt.xlabel("Number of Heads")
# plt.show()

#The longest walk you can take while getting home in 4 blocks or less 50% of the time is 22 blocks. 
#However, strangely, you won't be able to walk home in 4 blocks or less 50% of the time if
#you take a walk as short as 15 blocks long.

#A Monte carlo simulation is a simulation that takes in multiple ranges of values, usually including
#a minimum, maximum and average result, and uses them to calculate the likelyhood of each outcome
#which can be achieved by these ranges.

#The dart project seems to return ~3 for me most of the time I guess this means that 75% of the
#time you'll hit the board within 100 tries.


def walk(num):
	x = 0
	y = 0
	for i in range(0,num):
		r = random.randrange(0,4)
		if r == 0:
			x += 1
		elif r == 1:
			x -= 1
		elif r == 2:
			y += 1
		else:
			y -= 1
	dist = abs(x)+abs(y)
	return dist


def throw(num):
	hits = 0
	misses = 0
	for i in range(0,num):
		x = random.randrange(0,2)
		y = random.randrange(0,2)
		if math.sqrt(x**2+y**2) <= 1:
			if misses >= 100:
				misses = 0
			else:
				hits += 1
		else:	
			misses += 1
	return hits		


walkhome = 0
for x in range(1,31):
	for y in range(0,20000):
		if walk(x) <= 4:
			walkhome += 1
	print(str(x)+" -- "+str(walkhome/200)+"%")
	walkhome = 0


nums = 1000
for x in range(0,3):
	print(str(nums)+"--"+str(throw(nums)*4/nums))
	nums *= 10



	

