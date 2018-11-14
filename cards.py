import random
import sys
import os
import getch
import time
'''
https://stackoverflow.com/questions/10463201/getch-and-arrow-codes
'''

class card:
	def __init__(self):
		self.rank = 0
		self.suit = 0
		self.owner = 0
		self.id = 0
		self.picked = False
	def draw(self,xpos,ypos):
		if self.suit == "♦" or self.suit == "♥":
			sys.stdout.write("\u001b[31m")
		sys.stdout.write("\u001b["+str(ypos)+";"+str(xpos)+"H")
		print("╔═════╗")
		sys.stdout.write("\u001b["+str(ypos+1)+";"+str(xpos)+"H")
		if self.rank == 10:
			print("║"+str(self.rank)+"   ║")
		else:
			print("║"+str(self.rank)+"    ║")
		sys.stdout.write("\u001b["+str(ypos+2)+";"+str(xpos)+"H")
		print("║  "+str(self.suit)+"  ║")
		sys.stdout.write("\u001b["+str(ypos+3)+";"+str(xpos)+"H")
		if self.rank == 10:
			print("║   "+str(self.rank)+"║")
		else:
			print("║    "+str(self.rank)+"║")
		sys.stdout.write("\u001b["+str(ypos+4)+";"+str(xpos)+"H")
		print("╚═════╝")
		sys.stdout.write("\u001b[0m")

class deck:
	def __init__(self):
		self.cards = [card() for x in range(1,53)]
		for x in range(1,53):
			if x%13 == 10:
				self.cards[x-1].rank = "J"
			elif x%13 == 11:
				self.cards[x-1].rank = "Q"
			elif x%13 == 12:
				self.cards[x-1].rank = "K"
			elif x%13 == 0:
				self.cards[x-1].rank = "A"
			else:
				self.cards[x-1].rank = x%13+1
			if (x-1)//13 == 0:
				self.cards[x-1].suit = "♠"
			elif (x-1)//13 == 1:
				self.cards[x-1].suit = "♥"
			elif (x-1)//13 == 2:
				self.cards[x-1].suit = "♦"
			else:
				self.cards[x-1].suit = "♣"
		random.shuffle(self.cards)
	def transfer(self, card, new_owner):
		self.cards[card-1].owner = new_owner

os.system("clear")

deck1 = deck()
for x in range(1,53):
	deck1.cards[x-1].owner = 1
for x in range(14,27):
	deck1.cards[x-1].owner = 2
for x in range(27,40):
	deck1.cards[x-1].owner = 3
for x in range(40,53):
	deck1.cards[x-1].owner = 4

def select_cards(num, string):
	global winner
	global winnersuit
	global heartsbroken
	selected = 0
	done = False
	xval = 1
	while done == False:
		sys.stdout.write("\u001b[12;0H\u001b[0J")
		counter = 1
		for x in range(1,53):
			if deck1.cards[x-1].owner == 1:
				deck1.cards[x-1].id = 4*(counter)-3
				sys.stdout.write("\u001b[13;"+str(4*(counter)-3)+"H\u001b[4m")
				print(str(counter))
				sys.stdout.write("\u001b[0m")
				if deck1.cards[x-1].picked == True:
					deck1.cards[x-1].draw(4*(counter)-3,14)
				else:
					deck1.cards[x-1].draw(4*(counter)-3,15)
				counter += 1
		sys.stdout.write("\u001b[13;"+str(4*(counter)-3)+"H\u001b[4m")
		print("Go")
		sys.stdout.write("\u001b[0m\u001b[20;0H")
		print(string)
		sys.stdout.write("\u001b[12;"+str(xval)+"H")
		print("↓")

		while getch.getch() == "\033":
			getch.getch()
			char = getch.getch()
			if char == "A":
				#print("up")
				pass
			elif char == "B":
				#print("down")
				pass
			elif char == "C":
				if xval <= 4*(counter-1)-3:
					xval += 4
				sys.stdout.write("\u001b[12;"+str(xval)+"H\u001b[2K")
				print("↓")
			elif char == "D":
				if xval >= 4:
					xval -= 4
				sys.stdout.write("\u001b[12;"+str(xval)+"H\u001b[2K")
				print("↓")

		for x in range(1,53):
			if deck1.cards[x-1].owner == 1 and deck1.cards[x-1].id == xval:
				if num == 1:	
					if winner == 1:
						if counter == 14:
							if not deck1.cards[x-1].suit == "♣" or not deck1.cards[x-1].rank == 2:
								deck1.cards[x-1].picked = True
								selected += 1
								xval = 1
								string = "You have the two of clubs. You must play the two of clubs on the first trick."
						elif deck1.cards[x-1].suit == "♥" and heartsbroken == False:
							deck1.cards[x-1].picked = True
							selected += 1
							xval = 1
							string = "The hearts have not been broken, so you cannot lead with a heart."
						else:
							winnersuit = deck1.cards[x-1].suit
					elif not deck1.cards[x-1].suit == winnersuit and not winner == 1:
						hassuit = False
						for y in range(1,53):
							if deck1.cards[y-1].suit == winnersuit and deck1.cards[y-1].owner == 1:
								hassuit = True
						if hassuit == True:
							deck1.cards[x-1].picked = True
							selected += 1
							xval = 1
							string = "You must play a card of the same suit as the first one played in this trick."
						elif deck1.cards[x-1].suit == "♠" and deck1.cards[x-1].rank == "Q":
							heartsbroken = True
						elif deck1.cards[x-1].suit == "♥":
							heartsbroken = True
				if deck1.cards[x-1].picked == True:
					deck1.cards[x-1].picked = False
					selected = 0
					if num == 1:
						for y in range(7,13):
							sys.stdout.write("\u001b["+str(y)+";10H")
							print("       ")
					else:
						for y in range(7,13):
							sys.stdout.write("\u001b["+str(y)+";0H\u001b[2K")
					for y in range(1,53):
						if deck1.cards[y-1].picked == True and deck1.cards[y-1].owner == 1:
							deck1.cards[y-1].draw(10+4*selected,7)
							selected += 1
				elif selected <= num-1:
					deck1.cards[x-1].picked = True
					deck1.cards[x-1].draw(10+4*selected,7)
					selected += 1
				sys.stdout.write("\u001b[1;1H")
		if xval > 4*(counter-1)-3 and selected == num:
			done = True

def ai_trade_cards(owner):
	selected = 0
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].suit == "♠" and deck1.cards[x-1].rank == "A":
				if selected <= 2:
					deck1.cards[x-1].picked = True
					selected += 1
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].suit == "♠" and deck1.cards[x-1].rank == "K":
				if selected <= 2:
					deck1.cards[x-1].picked = True
					selected += 1
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].suit == "♥" and deck1.cards[x-1].rank == "A":
				if selected <= 2:
					deck1.cards[x-1].picked = True
					selected += 1
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].suit == "♥" and deck1.cards[x-1].rank == "Q":
				if selected <= 2:
					deck1.cards[x-1].picked = True
					selected += 1
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].suit == "♥" and deck1.cards[x-1].rank == "K":
				if selected <= 2:
					deck1.cards[x-1].picked = True
					selected += 1
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].suit == "♥" and deck1.cards[x-1].rank == "J":
				if selected <= 2:
					deck1.cards[x-1].picked = True
					selected += 1
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].rank == "A" and not deck1.cards[x-1].picked == True:
					if selected <= 2:
						deck1.cards[x-1].picked = True
						selected += 1
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].rank == "K" and not deck1.cards[x-1].picked == True:
					if selected <= 2:
						deck1.cards[x-1].picked = True
						selected += 1
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].rank == "Q" and not deck1.cards[x-1].picked == True:
					if selected <= 2:
						deck1.cards[x-1].picked = True
						selected += 1
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].rank == "J" and not deck1.cards[x-1].picked == True:
					if selected <= 2:
						deck1.cards[x-1].picked = True
						selected += 1
	for x in range(1,10):
		for y in range(1,53):
			if deck1.cards[y-1].owner == owner and deck1.cards[y-1].suit == "♥":
				if deck1.cards[y-1].rank == 11-x and not deck1.cards[y-1].picked == True:
					if selected <= 2:
						deck1.cards[y-1].picked = True
						selected += 1
	for x in range(1,10):
		for y in range(1,53):
			if deck1.cards[y-1].owner == owner:
				if deck1.cards[y-1].rank == 11-x and not deck1.cards[y-1].picked == True:
					if selected <= 2:
						deck1.cards[y-1].picked = True
						selected += 1

def ai_select_cards(owner):
	global winner
	global winnersuit
	global heartsbroken
	cardpicked = False
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].suit == "♣" and deck1.cards[x-1].rank == 2:
				deck1.cards[x-1].picked = True
				winnersuit = deck1.cards[x-1].suit
				cardpicked = True
	if owner == winner:
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and heartsbroken == False:
				if deck1.cards[x-1].suit == "♦" or deck1.cards[x-1].suit == "♣":
					if deck1.cards[x-1].rank == "A":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							winnersuit = deck1.cards[x-1].suit
							cardpicked = True
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and heartsbroken == False:
				if deck1.cards[x-1].suit == "♦" or deck1.cards[x-1].suit == "♣":
					if deck1.cards[x-1].rank == "K":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							winnersuit = deck1.cards[x-1].suit
							cardpicked = True
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and heartsbroken == False:
				if deck1.cards[x-1].suit == "♦" or deck1.cards[x-1].suit == "♣":
					if deck1.cards[x-1].rank == "Q":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							winnersuit = deck1.cards[x-1].suit
							cardpicked = True
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and heartsbroken == False:
				if deck1.cards[x-1].suit == "♦" or deck1.cards[x-1].suit == "♣":
					if deck1.cards[x-1].rank == "J":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							winnersuit = deck1.cards[x-1].suit
							cardpicked = True
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and heartsbroken == False:
				if deck1.cards[x-1].suit == "♠":
					if deck1.cards[x-1].rank == "J":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							winnersuit = deck1.cards[x-1].suit
							cardpicked = True
		for x in range(1,10):
			for y in range(1,53):
				if deck1.cards[y-1].owner == owner and heartsbroken == False:
					if not deck1.cards[y-1].suit == "♥":
						if deck1.cards[y-1].rank == 11-x:
							if cardpicked == False:
								deck1.cards[y-1].picked = True
								winnersuit = deck1.cards[y-1].suit
								cardpicked = True
		for x in range(2,10):
			for y in range(1,53):
				if deck1.cards[y-1].owner == owner and heartsbroken == True:
					if deck1.cards[y-1].rank == x:
						if cardpicked == False:
							deck1.cards[y-1].picked = True
							winnersuit = deck1.cards[y-1].suit
							cardpicked = True
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and heartsbroken == True:
				if deck1.cards[x-1].rank == "J":
					if cardpicked == False:
						deck1.cards[x-1].picked = True
						winnersuit = deck1.cards[x-1].suit
						cardpicked = True
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and heartsbroken == True:
				if deck1.cards[x-1].rank == "Q":
					if cardpicked == False:
						deck1.cards[x-1].picked = True
						winnersuit = deck1.cards[x-1].suit
						cardpicked = True
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and heartsbroken == True:
				if deck1.cards[x-1].rank == "K":
					if cardpicked == False:
						deck1.cards[x-1].picked = True
						winnersuit = deck1.cards[x-1].suit
						cardpicked = True
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and heartsbroken == True:
				if deck1.cards[x-1].rank == "A":
					if cardpicked == False:
						deck1.cards[x-1].picked = True
						winnersuit = deck1.cards[x-1].suit
						cardpicked = True
	else:
		hassuit = False
		for x in range(1,53):
			if deck1.cards[x-1].owner == owner and deck1.cards[x-1].suit == winnersuit:
				hassuit = True
		if hassuit == False:
			for x in range(1,53):
				if deck1.cards[x-1].picked == True and deck1.cards[x-1].suit == "♠":
					if deck1.cards[x-1].rank == "A" or deck1.cards[x-1].rank == "K":
						for y in range(1,53):
							if deck1.cards[y-1].owner == owner:
								if deck1.cards[y-1].suit == "♠" and deck1.cards[y-1].rank == "Q":
									if cardpicked == False:
										deck1.cards[y-1].picked == True
										heartsbroken = True
										cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].owner == owner:
					if deck1.cards[x-1].suit == "♥" and deck1.cards[x-1].rank == "A":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							heartsbroken = True
							cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].owner == owner:
					if deck1.cards[x-1].suit == "♥" and deck1.cards[x-1].rank == "K":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							heartsbroken = True
							cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].owner == owner:
					if deck1.cards[x-1].suit == "♥" and deck1.cards[x-1].rank == "Q":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							heartsbroken = True
							cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].owner == owner:
					if deck1.cards[x-1].suit == "♥" and deck1.cards[x-1].rank == "J":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							heartsbroken = True
							cardpicked = True
			for x in range(1,10):
				for y in range(1,53):
					if deck1.cards[y-1].owner == owner:
						if deck1.cards[y-1].suit == "♥" and deck1.cards[y-1].rank == 11-x:
							if cardpicked == False:
								deck1.cards[y-1].picked = True
								heartsbroken = True
								cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].owner == owner:
					if deck1.cards[x-1].rank == "A":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].owner == owner:
					if deck1.cards[x-1].rank == "K":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].owner == owner:
					if deck1.cards[x-1].rank == "Q":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].owner == owner:
					if deck1.cards[x-1].rank == "J":
						if cardpicked == False:
							deck1.cards[x-1].picked = True
							cardpicked = True
			for x in range(1,10):
				for y in range(1,53):
					if deck1.cards[y-1].owner == owner:
						if deck1.cards[y-1].rank == 11-x:
							if cardpicked == False:
								deck1.cards[y-1].picked = True
								cardpicked = True
		else:
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == False:
						if deck1.cards[x-1].rank == "A" and not deck1.cards[x-1].suit == "♠":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == False:
						if deck1.cards[x-1].rank == "K" and not deck1.cards[x-1].suit == "♠":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								winnersuit = deck1.cards[x-1].suit
								cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == False:
						if deck1.cards[x-1].rank == "Q":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								winnersuit = deck1.cards[x-1].suit
								cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == False:
						if deck1.cards[x-1].rank == "J":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								winnersuit = deck1.cards[x-1].suit
								cardpicked = True
			for x in range(1,10):
				for y in range(1,53):
					if deck1.cards[y-1].suit == winnersuit:
						if deck1.cards[y-1].owner == owner and heartsbroken == False:
							if deck1.cards[y-1].rank == 11-x:
								if cardpicked == False:
									deck1.cards[y-1].picked = True
									cardpicked = True
			for x in range(2,10):
				for y in range(1,53):
					if deck1.cards[y-1].suit == winnersuit:
						if deck1.cards[y-1].owner == owner and heartsbroken == True:
							if deck1.cards[y-1].rank == x:
								if cardpicked == False:
									deck1.cards[y-1].picked = True
									cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == True:
						if deck1.cards[x-1].rank == "J":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								winnersuit = deck1.cards[x-1].suit
								cardpicked = True	
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == True:
						if deck1.cards[x-1].rank == "Q":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								winnersuit = deck1.cards[x-1].suit
								cardpicked = True	
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == True:
						if deck1.cards[x-1].rank == "K":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								winnersuit = deck1.cards[x-1].suit
								cardpicked = True	
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == True:
						if deck1.cards[x-1].rank == "A":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								winnersuit = deck1.cards[x-1].suit
								cardpicked = True
	if owner == 2:
		for x in range(1,53):
			if deck1.cards[x-1].owner == 2 and deck1.cards[x-1].picked == True:
				deck1.cards[x-1].draw(3,4)
	if owner == 3:
		for x in range(1,53):
			if deck1.cards[x-1].owner == 3 and deck1.cards[x-1].picked == True:
				deck1.cards[x-1].draw(10,1)
	if owner == 4:
		for x in range(1,53):
			if deck1.cards[x-1].owner == 4 and deck1.cards[x-1].picked == True:
				deck1.cards[x-1].draw(17,4)

def determine_winner():
	global winner
	global winnersuit
	global heartsbroken
	winnerdetermined = False
	for x in range(1,53):
		if deck1.cards[x-1].suit == winnersuit and deck1.cards[x-1].picked == True:
			if deck1.cards[x-1].rank == "A" and winnerdetermined == False:
				winner = deck1.cards[x-1].owner
				winnerdetermined = True
	for x in range(1,53):
		if deck1.cards[x-1].suit == winnersuit and deck1.cards[x-1].picked == True:
			if deck1.cards[x-1].rank == "K" and winnerdetermined == False:
				winner = deck1.cards[x-1].owner
				winnerdetermined = True
	for x in range(1,53):
		if deck1.cards[x-1].suit == winnersuit and deck1.cards[x-1].picked == True:
			if deck1.cards[x-1].rank == "Q" and winnerdetermined == False:
				winner = deck1.cards[x-1].owner
				winnerdetermined = True
	for x in range(1,53):
		if deck1.cards[x-1].suit == winnersuit and deck1.cards[x-1].picked == True:
			if deck1.cards[x-1].rank == "J" and winnerdetermined == False:
				winner = deck1.cards[x-1].owner
				winnerdetermined = True
	for x in range(1,10):
		for y in range(1,53):
			if deck1.cards[y-1].suit == winnersuit and deck1.cards[y-1].picked == True:
				if deck1.cards[y-1].rank == 11-x and winnerdetermined == False:
					winner = deck1.cards[y-1].owner
					winnerdetermined = True
	for x in range(1,53):
		if deck1.cards[x-1].picked == True:
			deck1.cards[x-1].picked = False
			deck1.transfer(x,5)


winner = 0
winnersuit = "♣"
heartsbroken = False
select_cards(3,"Please choose three cards to trade.")
ai_trade_cards(2)
ai_trade_cards(3)
ai_trade_cards(4)

traded = 0
for x in range(1,53):
	if deck1.cards[x-1].owner == 4 and deck1.cards[x-1].picked == True: 
		deck1.cards[x-1].draw(10+4*traded,1)
		traded += 1 

sys.stdout.write("\u001b[3;25H")
print("Recieved")
sys.stdout.write("\u001b[9;25H")
print("Traded")
sys.stdout.write("\u001b[11;80H\u001b[1J")
time.sleep(3)

for x in range(1,53):
	for y in range(1,5):
		if deck1.cards[x-1].owner == y and deck1.cards[x-1].picked == True:
			deck1.cards[x-1].picked = False
			deck1.transfer(x,(y)%4+1)

for x in range(1,53):	
	if deck1.cards[x-1].rank == 2 and deck1.cards[x-1].suit == "♣":	
		winner = deck1.cards[x-1].owner

ended = False
while ended == False:
	if winner == 1:
		select_cards(1,"Please choose a card to play.")
		ai_select_cards(2)
		ai_select_cards(3)
		ai_select_cards(4)
	elif winner == 2:
		ai_select_cards(2)
		ai_select_cards(3)
		ai_select_cards(4)
		select_cards(1,"Please choose a card to play.")
	elif winner == 3:
		ai_select_cards(3)
		ai_select_cards(4)
		select_cards(1,"Please choose a card to play.")
		ai_select_cards(2)
	elif winner == 4:
		ai_select_cards(4)
		select_cards(1,"Please choose a card to play.")
		ai_select_cards(2)
		ai_select_cards(3)
	determine_winner()
	sys.stdout.write("\u001b[0;0H")
	print(str(winner))
	time.sleep(2)
	sys.stdout.write("\u001b[11;80H\u001b[1J")
	












