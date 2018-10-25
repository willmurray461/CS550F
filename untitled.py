import sjs
import random

size = int(sjs.argv[1])


solution = [[] for i in range(0,size+2)]
revealed = [[] for i in range(0,size+2)]
for i in range(0,size+2):
	solution[i] = [0]*(size+2)
for i in range(0,size+2):
	revealed[i] = []*(size+2)

def add_mines():
	for i in range(0,int(size**2/5)):
		solution[random.randrange(1,size+1)][random.randrange(1,size+1)] = "*"

def add_numbers():
	for i in range(1,size+1):
		for j in range(1,size+1):
			if solution[i][j] == "*":
				if not solution[i-1][j] == "*":
					solution[i-1][j] +=1
				if not solution[i][j-1] == "*":
					solution[i][j-1] +=1
				if not solution[i+1][j] == "*":
					solution[i+1][j] +=1
				if not solution[i][j+1] == "*":
					solution[i][j+1] +=1
				if not solution[i-1][j-1] == "*":
					solution[i-1][j-1] +=1
				if not solution[i+1][j+1] == "*":
					solution[i+1][j+1] +=1
				if not solution[i-1][j+1] == "*":
					solution[i-1][j+1] +=1
				if not solution[i+1][j-1] == "*":
					solution[i+1][j-1] +=1

def reveal():
	#Take input, then set revealed[inputx][inputy] to solution[x][y]
	for k in range(0,size**2):
		for i in range(1,size+1):
			for j in range(1,size+1):
				if revealed[i][j] == solution[i][j] == 0:
					revealed[i-1][j] = solution[i-1][j]
					revealed[i][j-1] = solution[i][j-1]
					revealed[i+1][j] = solution[i+1][j]
					revealed[i][j+1] = solution[i][j+1]
					revealed[i-1][j-1] = solution[i-1][j-1]
					revealed[i+1][j+1] = solution[i+1][j+1]
					revealed[i-1][j+1] = solution[i-1][j+1]
					revealed[i+1][j-1] = solution[i+1][j-1]
	for i in range(1,size+1):
		for j in range(1,size+1):
			if revealed[x][y] == "*":
				#you lose
	for i in range(0, size+2):
		print(*revealed[i])

add_mines()
add_numbers()
#while not losing:
#reveal()