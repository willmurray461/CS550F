import sys
import random

def Minesweeper(columns, rows, difficulty):
	outcome = 0
	field = [[] for x in range(0,rows+2)]
	facade = [[] for x in range(0,rows+2)]
	revealed = [[] for x in range(0,rows+2)]
	for x in range(0,rows+2):
		field[x] = [0]*(columns+2)
	for x in range(0,rows+2):
		facade[x] = ["⏹️"]*(columns+2)
	for x in range(0,rows+2):
		revealed[x] = [-1]*(columns+2)
	for x in range(0,int(rows*columns*difficulty/9)):
		field[random.randrange(1,rows+1)][random.randrange(1,columns+1)] = 9
	for x in range(1,rows+1):
		for y in range(1,columns+1):
			if field[x][y] == 9:
				if not field[x-1][y] == 9:
					field[x-1][y] +=1
				if not field[x][y-1] == 9:
					field[x][y-1] +=1
				if not field[x+1][y] == 9:
					field[x+1][y] +=1
				if not field[x][y+1] == 9:
					field[x][y+1] +=1
				if not field[x-1][y-1] == 9:
					field[x-1][y-1] +=1
				if not field[x+1][y+1] == 9:
					field[x+1][y+1] +=1
				if not field[x-1][y+1] == 9:
					field[x-1][y+1] +=1
				if not field[x+1][y-1] == 9:
					field[x+1][y-1] +=1
	for x in range(0,columns+1):
		facade[0][x] = "#️⃣"
	for x in range(0,columns+1):
		facade[rows+1][x] = "#️⃣"
	for x in range(0,rows+1):
		facade[x][0] = "#️⃣"
	for x in range(0,rows+1):
		facade[x][columns+1] = "#️⃣"
	facade[columns+1][rows+1] = "#️⃣"
	while outcome == 0:
		for x in range(0,rows*columns - int(rows*columns*difficulty/9)):
			for x in range(1,rows+1):
				for y in range(1,columns+1):
					if revealed[x][y] == field[x][y] == 0:
						revealed[x-1][y] = field[x-1][y]
						revealed[x][y-1] = field[x][y-1]
						revealed[x+1][y] = field[x+1][y]
						revealed[x][y+1] = field[x][y+1]
						revealed[x-1][y-1] = field[x-1][y-1]
						revealed[x+1][y+1] = field[x+1][y+1]
						revealed[x-1][y+1] = field[x-1][y+1]
						revealed[x+1][y-1] = field[x+1][y-1]
						facade[x][y] = "0️⃣"
		for x in range(1,rows+1):
			for y in range(1,columns+1):
				if revealed[x][y] == field[x][y]:
					if field[x][y] == 0:
						facade[x][y] = "0️⃣"
					elif field[x][y] == 1:
						facade[x][y] = "1️⃣"
					elif field[x][y] == 2:
						facade[x][y] = "2️⃣"
					elif field[x][y] == 3:
						facade[x][y] = "3️⃣"
					elif field[x][y] == 4:
						facade[x][y] = "4️⃣"
					elif field[x][y] == 5:
						facade[x][y] = "5️⃣"
					elif field[x][y] == 6:
						facade[x][y] = "6️⃣"
					elif field[x][y] == 7:
						facade[x][y] = "7️⃣"
					elif field[x][y] == 8:
						facade[x][y] = "8️⃣"
					elif field[x][y] == 9:
						facade[x][y] = "💣"
						outcome = 2
		if len(revealed) == rows * columns - rows*columns*difficulty/9 and 9 not in revealed:
			outcome = 1
		print("\n"*24)	
		for x in range(0,rows+2):
			print(*facade[x])
		if outcome == 0:
			xcoord = int(input("Enter the x coordinate of the tile you would like to sweep: "))
			ycoord = int(input("Enter the y coordinate of the tile you would like to sweep: "))
			revealed[ycoord][xcoord] = field[ycoord][xcoord]
		if outcome == 1:
			for x in range(1,rows+1):
				for y in range(1,columns+1):
					if field[x][y] == 9:
						facade[x][y] = "🚩"
			print("\n"*24)	
			for x in range(0,rows+2):
				print(*facade[x])
			print("You Win!")
			exit()
		if outcome == 2:
			print("You Lose. You uncovered a mine at",xcoord,"\b,",ycoord,"\b.")
			exit()
Minesweeper(16,16,2)
# ⏹️
# 1️⃣
# 2️⃣
# 3️⃣
# 4️⃣
# 5️⃣
# 6️⃣
# 7️⃣
# 8️⃣
# 💣
# 🚩





