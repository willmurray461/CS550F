# This Imports the necessary modules
import random
import sys
import os
import getch
import time

'''
https://stackoverflow.com/questions/10463201/getch-and-arrow-codes

was used to help understand getch
'''

#This is the card class used to create the 52 playing cards in a deck
class card:

	#This is the constructor, which gives each card certain values
	def __init__(self):

		# rank = rank e.g. 2-10, J, Q, K, A
		self.rank = 0

		# suit = suit e.g. Spades, Hearts, Diamonds, Clubs
		self.suit = 0

		# owner = the player who has the card in their hand
		self.owner = 0

		# id is used to help the process of selecting cards in the GUI
		self.id = 0

		# picked determines whether or not a card has been selected for play in a trick
		self.picked = False

	# This method draws the card in the GUI
	def draw(self,xpos,ypos):

		# This colors the cards red if they are hearts or diamonds
		if self.suit == "♦" or self.suit == "♥":
			sys.stdout.write("\u001b[31m")

		# This draws the card at the right coordinates
		# by moving the cursor to the correct spot and
		# drawing a line of text
		sys.stdout.write("\u001b["+str(ypos)+";"+str(xpos)+"H")
		print("╔═════╗")
		sys.stdout.write("\u001b["+str(ypos+1)+";"+str(xpos)+"H")

		# This if/else statement fixes a graphical issue when printing "10" 
		# because it is two characters long, unlike any other rank
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

		# This resets the terminal text color back to black
		sys.stdout.write("\u001b[0m")

# This is the deck class which contains the 52 playing cards
class deck:

	# This constructor which creates a standard deck of 52 playing cards
	def __init__(self):

		# This  creats a list of 52 cards using the card class
		self.cards = [card() for x in range(1,53)]

		# It then assigns each card a unique rank and suit combination which creates
		# a standard deck of playing cards
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

		# This then shuffles the cards
		random.shuffle(self.cards)

	# This method allows for easy transfer of cards between players' hands
	def transfer(self, card, new_owner):
		self.cards[card-1].owner = new_owner

#This clears the screen
os.system("clear")

#This creates a deck called deck1
deck1 = deck()

#This divides up the cards in deck1 between four players
for x in range(1,53):
	deck1.cards[x-1].owner = 1
for x in range(14,27):
	deck1.cards[x-1].owner = 2
for x in range(27,40):
	deck1.cards[x-1].owner = 3
for x in range(40,53):
	deck1.cards[x-1].owner = 4

#This function creates a GUI which allows the player to select cards in their hand for play
def select_cards(num, string):

	# Variables, such as the winner of the previous trick,
	# the suit of the first card that was played this trick,
	# and whether or not the hearts have been broken are used
	global winner
	global winnersuit
	global heartsbroken

	# This is a variable which keeps track of how many cards have been selected for play
	# every time this function is called it is set to 0
	selected = 0
	
	# This is a variable used to keep track of whether or not the player has selected
	# all of the cards they want to play this trick
	done = False

	# This is a variable which keeps track of the position of the cursor for the GUI
	xval = 1

	#This is the GUI that keeps running until all of the user's cards are selected
	while done == False:

		# This displays the scores and stats on the screen
		# again by moving the cursor to specific coordinates
		# and printing values
		for x in range(1,5):
			sys.stdout.write("\u001b["+str(x)+";40H")
			print("Player "+str(x)+": "+str(scores[x-1]))
		sys.stdout.write("\u001b[5;40H\u001b[0K")
		print("Hearts Broken = "+str(heartsbroken))
		sys.stdout.write("\u001b[12;0H\u001b[0J")

		# This is a counter to display how many cards the player has
		counter = 1

		# This for loop prints a number above each card, as well as the cards themselves
		for x in range(1,53):
			if deck1.cards[x-1].owner == 1:
				deck1.cards[x-1].id = 4*(counter)-3
				sys.stdout.write("\u001b[13;"+str(4*(counter)-3)+"H\u001b[4m")
				print(str(counter))
				sys.stdout.write("\u001b[0m")
				# This if statment raises the cards if they are currently selected
				if deck1.cards[x-1].picked == True:
					deck1.cards[x-1].draw(4*(counter)-3,14)
				else:
					deck1.cards[x-1].draw(4*(counter)-3,15)
				counter += 1

		# This prints a go button
		sys.stdout.write("\u001b[13;"+str(4*(counter)-3)+"H\u001b[4m")
		print("Go")

		# This prints a message at the bottom of the cards, 
		# which will change depending on the situation
		sys.stdout.write("\u001b[0m\u001b[20;0H")
		print(string)

		#This prints the cursor above the number of each card
		sys.stdout.write("\u001b[12;"+str(xval)+"H")
		print("↓")

		# This takes keyboard imput from the user using the getch library
		# This looks for the escape sequences of the left and right arrow keys
		# If either key is pressed, than the cursor is moved. Otherwise,
		# the loop ends and selects the card wherever the curser last was
		while getch.getch() == "\033":
			getch.getch()
			char = getch.getch()
			if char == "A":
				#print("up")
				pass
			elif char == "B":
				#print("down")
				pass

			# This moves the cursor right and updates its x position
			# when the right arrow key is pressed
			elif char == "C":
				if xval <= 4*(counter-1)-3:
					xval += 4
				sys.stdout.write("\u001b[12;"+str(xval)+"H\u001b[2K")
				print("↓")

			# This moves the cursor left and updates its x position
			# when the right arrow key is pressed
			elif char == "D":
				if xval >= 4:
					xval -= 4
				sys.stdout.write("\u001b[12;"+str(xval)+"H\u001b[2K")
				print("↓")

		# This selects the card wherever the cursor was on top of
		for x in range(1,53):
			if deck1.cards[x-1].owner == 1 and deck1.cards[x-1].id == xval:

				# This ariable is used to check how many cards the player is going to select
				# e.g. three for trading, one for normal gameplay
				if num == 1:

					# This first if statement makes sure that if the player has the two of clubs
					# that it plays it on the first turn	
					if winner == 1:
						if counter == 14:
							if not deck1.cards[x-1].suit == "♣" or not deck1.cards[x-1].rank == 2:
								deck1.cards[x-1].picked = True
								selected += 1
								xval = 1
								string = "You have the two of clubs. You must play the two of clubs on the first trick."

						# This other if statement makes sure the player doesn't
						# lead with a heart unless the hearts have been broken
						elif deck1.cards[x-1].suit == "♥" and heartsbroken == False:
							deck1.cards[x-1].picked = True
							selected += 1
							xval = 1
							string = "The hearts have not been broken, so you cannot lead with a heart."
						
						# This tells the program the suit of the first ard played in the trick
						else:
							winnersuit = deck1.cards[x-1].suit
					
					# This checks if the player has a card of the same suit of
					# the first ard played in the trick, and forces it
					# to play one if it has one
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
						
						# This tells the progtam that the hearts have been broken
						# if a heart or the queen of spades has been played 
						elif deck1.cards[x-1].suit == "♠" and deck1.cards[x-1].rank == "Q":
							heartsbroken = True
						elif deck1.cards[x-1].suit == "♥":
							heartsbroken = True

				# This deselects a card if it has already been selected,
				# and selects it if it has not
				# It also draws and erases the cards, and makes sure
				# that the exact right amout of cards has been selected
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

		# This ends the function if the right number of cards has been
		# selected and the go button has been pressed
		if xval > 4*(counter-1)-3 and selected == num:
			done = True

	#This writes down the stats again
	for x in range(1,5):
		sys.stdout.write("\u001b["+str(x)+";40H")
		print("Player "+str(x)+": "+str(scores[x-1]))
	sys.stdout.write("\u001b[5;40H\u001b[0K")
	print("Hearts Broken = "+str(heartsbroken))

#This function defines what the computer does when deciding which cards to trade
def ai_trade_cards(owner):
	
	#This variable determines how many cards have been picked
	selected = 0

	'''
	Basically, the function sets up a priority list of cards to trade.
	1) Trade the ace king or queen of spades
	2) Trade face card hearts
	3) Trade any face card
	4) Trade high hearts
	5) Trade high cards
	'''

	# The function is made of several loops that search for specific cards
	# The reason why there is a loop for each card is because that is
	# The only way I could think of that the loop would search the entire
	# deck for a specific card instead of one of several cards
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
			if deck1.cards[x-1].suit == "♠" and deck1.cards[x-1].rank == "Q":
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
	
	# This prints the stats again
	for x in range(1,5):
		sys.stdout.write("\u001b["+str(x)+";40H")
		print("Player "+str(x)+": "+str(scores[x-1]))
	sys.stdout.write("\u001b[5;40H\u001b[0K")
	print("Hearts Broken = "+str(heartsbroken))

# This function tells the computer which cards to pick during play
def ai_select_cards(owner):
	
	# It needs to know the player who won the previous trick,
	# the suit of the first card played this trick,
	# and whether or not the hearts have been broken
	global winner
	global winnersuit
	global heartsbroken

	#This variable tells the computer whether or not the AI has picked its card yet
	cardpicked = False

	'''
	This function behaves similarly to the ai trading cards function,
	however it is a little more complex
	It sets up a hierarchy like before, but with a few variables involved
	It is as follows:
	1) Play the two of clubs on the first round if you have it
	If the AI just won the last round:
		If the hearts are not broken:
		1) Pick face card diamonds or clubs
		2) Pick the jack of spades
		3) Pick high cards if they are not hearts
		If the hearts are broken:
		1) Pick low cards
		2) Pick low royalty
	If the AI didn't win the last round
		If you have a card that is of the same suit as the first
		card played in the trick:
			If the hearts are not broken:
			1) Pick face cards that are of the same suit as the first
			card played in the trick
			2) Pick high cards that are of the same suit as the first
			card played in the trick
			If the hearts are broken:
			1) play low cards that are of the same suit as the first
			card played in the trick
			2) play face cards that are of the same suit as the first
			card played in the trick
		If you don't have a card that is of the same suit as the first
		card played in the trick:
			1) If you have it, play the queen of spades
			2) Play the highest heart you have
			3) Play the higest card you have
	'''

	# Again this function is made of several loops that search for specific cards
	for x in range(1,53):
		if deck1.cards[x-1].owner == owner:
			if deck1.cards[x-1].suit == "♣" and deck1.cards[x-1].rank == 2:
				deck1.cards[x-1].picked = True
				# This makes sure that the computer knows what the suit of the
				# card that was played first in this trick was
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
							# This tells the computer that the hearts have been broken
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
				if deck1.cards[x-1].picked == True and deck1.cards[x-1].suit == "♠":
					if deck1.cards[x-1].rank == "A" or deck1.cards[x-1].rank == "K":
						for y in range(1,53):
							if deck1.cards[y-1].owner == owner and deck1.cards[y-1].suit == winnersuit:
								if deck1.cards[y-1].suit == "♠" and deck1.cards[y-1].rank == "Q":
									if cardpicked == False:
										deck1.cards[y-1].picked == True
										heartsbroken = True
										cardpicked = True
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
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == False:
						if deck1.cards[x-1].rank == "K" and deck1.cards[x-1].suit == "♠":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								winnersuit = deck1.cards[x-1].suit
								cardpicked = True
			for x in range(1,53):
				if deck1.cards[x-1].suit == winnersuit:
					if deck1.cards[x-1].owner == owner and heartsbroken == False:
						if deck1.cards[x-1].rank == "A" and deck1.cards[x-1].suit == "♠":
							if cardpicked == False:
								deck1.cards[x-1].picked = True
								winnersuit = deck1.cards[x-1].suit
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
	
	# This draws the card the AI selected on the screen in the correct position
	# depending upon which player it is
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
	
	# This draws the stats again
	for x in range(1,5):
		sys.stdout.write("\u001b["+str(x)+";40H")
		print("Player "+str(x)+": "+str(scores[x-1]))
	sys.stdout.write("\u001b[5;40H\u001b[0K")
	print("Hearts Broken = "+str(heartsbroken))

# This function is used to determine the winner of each trick
def determine_winner():
	# This function takes in a list scores, which is a list 
	# which contains the score of each player, as well as
	# variables which we have seen before
	global scores
	global winner
	global winnersuit
	global heartsbroken

	# This creates a variable which tells the function only to declare
	# a winner if one has not already been declared
	winnerdetermined = False
	# These for loops find the highest card of the same suit
	# of the first card that was play in this trick

	# These for loops look for specific cards starting with the face cards
	# and then the number cards
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
			if deck1.cards[x-1].suit == "♠" and deck1.cards[x-1].rank == "Q":
				scores[winner-1] += 13
			if deck1.cards[x-1].suit == "♥":
				scores[winner-1] += 1
	
	#This displays the winner of each trick after each player has selected a card
	sys.stdout.write("\u001b[7;30H")
	print("Player "+str(winner)+" Wins!")
	
	# This prints the stats again
	for x in range(1,5):
		sys.stdout.write("\u001b["+str(x)+";40H")
		print("Player "+str(x)+": "+str(scores[x-1]))
	sys.stdout.write("\u001b[5;40H\u001b[0K")
	print("Hearts Broken = "+str(heartsbroken))
	
	# After the winner has been determined, the cards are discarded
	# by giving them to another nonexistent player's hand
	for x in range(1,53):
		if deck1.cards[x-1].picked == True:
			deck1.cards[x-1].picked = False
			deck1.transfer(x,5)



# This creates the list of players' scores
scores = [0 for x in range(1,5)]

# This creates a variable which shows the winner of the trick and who will go first next round
winner = 0

# This creates a variable which shows the suit of the first card played in the trick
winnersuit = "♣"

# This creates a variable which tells the computer whether or not the hearts have been broken
heartsbroken = False

# This tells the player to select three cards to trade
select_cards(3,"Please choose three cards to trade.")

# This tells the AI to make their trades
ai_trade_cards(2)
ai_trade_cards(3)
ai_trade_cards(4)

# This loop is used to draw the traded  and recievedcards
# This variable is used to aid the GUI in drawing the traded cards
traded = 0
for x in range(1,53):
	if deck1.cards[x-1].owner == 4 and deck1.cards[x-1].picked == True: 
		deck1.cards[x-1].draw(10+4*traded,1)
		traded += 1 

# This draws text on the screen which is part of the GUI;
# it tells the player which cards he traded and recieved
sys.stdout.write("\u001b[3;25H")
print("Recieved")
sys.stdout.write("\u001b[9;25H")
print("Traded")
sys.stdout.write("\u001b[11;80H\u001b[1J")
time.sleep(3)

# This loop transfers the cards between players
for x in range(1,53):
	for y in range(1,5):
		if deck1.cards[x-1].owner == y and deck1.cards[x-1].picked == True:
			deck1.cards[x-1].picked = False
			deck1.transfer(x,(y)%4+1)

# This tells the computer that whoever has the two of clubs needs to go first
for x in range(1,53):	
	if deck1.cards[x-1].rank == 2 and deck1.cards[x-1].suit == "♣":	
		winner = deck1.cards[x-1].owner

# This loop tells the players to pick cards until the game is over
ended = False
while ended == False:

	# These if statements determine the order of players depending on who won the last trick
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
	
	# Once the players have selected their cards, this determines the winner
	determine_winner()
	ended = True 
	# If all players are out of cards, this ends the loop
	for x in range(1,53):
		if not deck1.cards[x-1].owner == 5:
			ended = False
	time.sleep(2)
	sys.stdout.write("\u001b[11;80H\u001b[1J")

# This prints the final stats on the board
os.system("clear")
sys.stdout.write("\u001b[6;6H")
print("Game Over")
sys.stdout.write("\u001b[6;6H")
print("Final Score:")
for x in range(9,13):
		sys.stdout.write("\u001b["+str(x)+";6H")
		print("Player "+str(x)+": "+str(scores[x-9]))

	












