import random
import sys
import os
import getch
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
		if self.rank == "10":
			print("║"+str(self.rank)+"   ║")
		else:
			print("║"+str(self.rank)+"    ║")
		sys.stdout.write("\u001b["+str(ypos+2)+";"+str(xpos)+"H")
		print("║  "+str(self.suit)+"  ║")
		sys.stdout.write("\u001b["+str(ypos+3)+";"+str(xpos)+"H")
		if self.rank == "10":
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
		for x in range(1,50000):
			rand1 = random.randrange(0,52)
			rand2 = random.randrange(0,52)
			tempvar = self.cards[rand1]
			self.cards[rand1] = self.cards[rand2]
			self.cards[rand2] = tempvar
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
	selected = 0
	done = False
	while done == False:
		os.system("clear")
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
		sys.stdout.write("\u001b[12;0H")
		print("↓")

		xval = 1
		while getch.getch() == "\033":
			getch.getch()
			char = getch.getch()
			if char == "A":
				print("up")
			elif char == "B":
				print("down")
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

		if xval > 4*(counter-1)-7 and selected == num:
			done = True

		for x in range(1,53):
			if deck1.cards[x-1].owner == 1:
				if deck1.cards[x-1].id == xval:
					if deck1.cards[x-1].picked == True:
						deck1.cards[x-1].picked = False
						selected -= 1
					elif selected <= num-1:
						deck1.cards[x-1].picked = True
						selected += 1

def ai_trade_cards(owner):
	selected = 0
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].suit == "♠":
				if deck1.cards[x-1].suit == "K" or deck1.cards[x-1].suit == "A":
					if selected <= 2:
						deck1.cards[x-1].picked = True
						selected +=1
			elif deck1.cards[x-1].suit == "♥":
				if deck1.cards[x-1].rank == "J" or deck1.cards[x-1].rank == "Q" or deck1.cards[x-1].rank == "K" or deck1.cards[x-1].rank == "A":
					if selected <= 2:
						deck1.cards[x-1].picked = True
						selected +=1
			elif deck1.cards[x-1].rank == "J" or deck1.cards[x-1].rank == "Q" or deck1.cards[x-1].rank == "K" or deck1.cards[x-1].rank == "A":
					if selected <= 2:
						deck1.cards[x-1].picked = True
						selected +=1
			else:
				for x in range(1,10):
					if deck1.cards[x-1].rank == 11-x:
						if selected <= 2:
							deck1.cards[x-1].picked == True
							selected +=1

def determine_winner(winnersuit, winner):
	for x in range(1,53)
		if deck1.cards[x-1].suit == winnersuit and deck1.cards[x-1].picked == True:
			cardsplayed = [x for x in range(1,5)]
			cardsplayed.append(deck1.cards[x-1].rank)
		if deck1.cards[x-1].rank == max(cardsplayed[]):
			winner = deck1.cards[x-1].owner

def ai_select_cards(owner, winnersuit, heartsbroken):




'''

AI Notes:

on trade:
highest priority is ace of spades & king of spades
next highest priority is high hearts,
then trade high anything else that is high

during play:
if has 2 of clubs, play it
must play suit that previous round's winner chooses, unless unable to do so
while hearts are not broken, play high clubs and diamonds, and any spades J or lower
after hearts are broken, play low cards
if cannot play a suit, play high hearts or Q or higher of spades

'''
winner = 0
select_cards(3,"Please choose three cards to trade.")
ai_trade_cards(2)
ai_trade_cards(3)
ai_trade_cards(4)
for x in range(1,53):
	for y in range(1,5):
		if deck1.cards[x-1].owner == y and deck1.cards[x-1].picked == True:
			deck1.cards[x-1].picked = False
			deck1.transfer(x,(y)%4+1)

for x in range(1,53):	
	if deck1.cards[x-1].rank == 2 and deck1.cards[x-1].suit == "♣" and deck1.cards[x-1].owner == 1 and deck1.cards[x-1].picked == False:	
		winner = deck1.cards[x-1].owner

if winner == 1:
	select_cards(1,"Please choose a card to play.")
elif winner == 2:
	ai_select_cards(2, winnersuit, heartsbroken)
	ai_select_cards(3, winnersuit, heartsbroken)
	ai_select_cards(4, winnersuit, heartsbroken)
	select_cards(1,"Please choose a card to play.")
elif winner == 3:
	ai_select_cards(3, winnersuit, heartsbroken)
	ai_select_cards(4, winnersuit, heartsbroken)
	select_cards(1,"Please choose a card to play.")
	ai_select_cards(2, winnersuit, heartsbroken)
elif winner == 4:
	ai_select_cards(4, winnersuit, heartsbroken)
	select_cards(1,"Please choose a card to play.")
	ai_select_cards(2, winnersuit, heartsbroken)
	ai_select_cards(3, winnersuit, heartsbroken)

#AI picks cards
twoofclubs = True
for x in range(1,53):	
	if deck1.cards[x-1].rank == 2 and deck1.cards[x-1].suit == "♣" and deck1.cards[x-1].owner == 1 and deck1.cards[x-1].picked == False:	
		twoofclubs = False
while twoofclubs == False:
	for x in range(1,53):
		if deck1.cards[x-1].owner == 1 and deck1.cards[x-1].picked == True:
			deck1.cards[x-1].picked = False
	select_cards(1,"You have the 2 of clubs. The 2 of clubs must be played on the first round.")
	for x in range(1,53):	
		if deck1.cards[x-1].rank == 2 and deck1.cards[x-1].suit == "♣" and deck1.cards[x-1].owner == 1 and deck1.cards[x-1].picked == True:	
			twoofclubs = True
# for x in range(1,53):
# 		for y in range(1,5):
# 			if deck1.cards[x-1].owner == y and deck1.cards[x-1].picked == True:
# 				deck1.cards[x-1].picked = False
# 				deck1.transfer(x,5)
		
heartsbroken = False
ended = False
while ended == False:
	select_cards(1,"Please choose a card to play.")
	# for x in range(1,53):
	# 	for y in range(1,5):
	# 		if deck1.cards[x-1].owner == y and deck1.cards[x-1].picked == True:
	# 			deck1.cards[x-1].picked = False
	# 			deck1.transfer(x,5)
	#AI picks cards
	#for x in range():
	


















