import sys
import time
def start():
	for x in range(1,7):
		print("Loading |")
		time.sleep(0.2)
		sys.stdout.write("\033[F")
		print("Loading /")
		time.sleep(0.2)
		sys.stdout.write("\033[F")
		print("Loading ─")
		time.sleep(0.2)
		sys.stdout.write("\033[F")
		print("Loading \\")
		time.sleep(0.2)
		sys.stdout.write("\033[F")
		for x in range(1,24):
				print("\n")
		for x in range(1,24):
			sys.stdout.write("\033[F")
	print("                               ╔═══════════════╗")
	print("                               ║TEXT ADVENTURE!║")
	print("                               ╚═══════════════╝")
	print("                               By: William Murray")
	print("                             ©willmurray461 9/24/18\n")
	startanswer = str.lower(input("Greetings user!\n\n\tWelcome to text adventure, an adventure made entirely from ASCII text.\nIf you accidentally opened this program and want to leave, type 'quit,'\notherwise press 'continue' to continue.\n\nUser:\\> "))
	validstart = False
	while validstart == False:
		if startanswer == "continue":
			validstart = True
			print("OK! Now, on to the text adventure!")
			time.sleep(1.0)
			start = str.lower(input("\n\tThrough some backstory which I am not in the mood to tell right now, you\nhave come into possession of a treasure map. This map tells you that there is\nsome treasure at a specific location which you decide to go to. Dissapointingly,\nyou only find more instructions on how to find the treasure. The instructions\nsay that you need to first travel to a remote part of a rainforest in Mexico.\nDo you want to:\nA: Buy plane tickets to the nearest airport.\nB: Take a bus into the location.\nC: Give up and look for the treasure another time.\nType [A/B/C]\n\nUser:\\> "))
			validstartanswer = False
			while validstartanswer == False:
				if start == "a":
					validstartanswer = True
					print("That's the sensible decision...\n")
					time.sleep(1.0)
					starta()
				elif start == "b":
					validstartanswer = True
					print("Interesting choice...\n")
					time.sleep(1.0)
					startb()
				elif start == "c":
					validstartanswer = True
					print("Really? OK then...\n")
					time.sleep(1.0)
					startc()
				else:
					sys.stdout.write("\033[F")
					sys.stdout.write("\033[F")
					start = str.lower(input("Type either 'a,' 'b,' or 'c' to choose an option.\nUser:\\> "))
					# start = str.lower(input(("User:\\> ")))
		elif startanswer == "quit":
			exit()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			startanswer = input("Type 'continue' to continue or 'quit' to exit the program.\nUser:\\> ")
def starta():
	astart = str.lower(input("\tYou arrive at the nearest airport which is still 20 miles from where\nthe maptells you to go. You decide that you should try to take a bus\nto yourdestinaiton, but since you don't speak spanish, you take the wrong\nbus andaccidentally get lost. Fortunately, the bus you accidentally take leads\nyou to apopular tourist site where you find a hotel in which people speak\nenglish.The man at the front desk tells you which public bus to take, but says\nyou'll still need to walk a couple miles from the bus stop to get to your\ndestination. Another man says he knows a better way into the part of the forest\nyou need to go to, but he looks pretty sketchy. Do you want to:\nA: Take the bus the hotel guy told you to take.\nB: Use the sketchy guy's route.\n\nUser:\\>"))
	validastart = False
	while validastart == False:
		if astart == "a":
			validastart = True
			print("Good call...\n")
			ime.sleep(1.0)
			startb()
		if astart == "b":
			validastart = True
			print("Hmmm...OK...\n")
			time.sleep(1.0)
			ab()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			astart = str.lower(input("Type 'a' or 'b' to choose an option.\nUser:\\> "))
def startb():
	print("\tAfter taking your busse(s), you got to your destination. At least, you\n got close to your destination. You still need to walk to the specified location on the map. The map says as follows:")
	print("╔══════════════════════════════════════════════════════════════════════╗")
	print("║         ^                  Treasure Map:                             ║")
	print("║       ^^^^^    <–––––––––– Mountain                                  ║")
	print("║      ^^ ^^ ^^                                                        ║")
	print("║    ^^  ^^ ^^ ^^                                                      ║")
	print("║    ^^ ^ ^ ^^^ ^ ^ =================                                  ║")
	print("║  ^ ^ ^^^ ^ ^ ^^^                 ||   <---------- Unecessarily Long  ║")
	print("║     (TREASURE)      XX           ||               Winding Path       ║")
	print("║ XX XXXX        XX XXXX           ===============                     ║")
	print("║XXXX ||XXXX  XX XXXX ||XXXX  XX                 ||                    ║")
	print("║ ||  XX ||  XXXX ||  XX ||  XXXX                ==========            ║")
	print("║ XX XXXXXXXXX||  XX XXXXXXXXX||                         ||            ║")
	print("║XXXX ||  ||     XXXX ||  ||                       ======||            ║")
	print("║ ||       XX                                      ||                  ║")
	print("║      XX XXXX    <------------- Forest            ||                  ║")
	print("║     XXXX ||XXXX  XX                              ||                  ║")
	print("║      ||  XX ||  XXXX                             ||                  ║")
	print("║      XX XXXXXXXXX||     =========================||                  ║")
	print("║     XXXX ||  ||       ✘ <-------------- You are Here                 ║")
	print("╚══════════════════════════════════════════════════════════════════════╝")
	time.sleep(7.0)
	bstart = str.lower(input("\nWould you like to:\nA: Go through the forest.\nB: Take the dirt path around.\n\nUser:\\> "))
	validbstart = False
	while validbstart == False:
		if bstart == "a":
			validbstart = True
			print("I see you're the adventurous type!\n")
			time.sleep(1.0)
			ba()
		if bstart == "b":
			validbstart = True
			print("I see you're the careful type!\n")
			time.sleep(1.0)
			bb()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			bstart = str.lower(input("Type either 'a,' 'b,' or 'c' to choose an option.\nUser:\\> "))
def startc():
	cstart = str.lower(input("\tSo you give up on trying to find the treasure and decide to put the map\naway. I guess treasure hunting just isn't for you.\nTHE END.\nWow, you're really boring...\nWant to play again? [Y/N]\n\nUser:\\> "))
	validcstart = False
	while validcstart == False:
		if cstart == "y":
			validcstart = True
			print("Nice to see you again...\n")
			time.sleep(1.0)
			start()
		if cstart == "n":
			validcstart = True
			print("Goodbye!\n")
			time.sleep(1.0)
			exit()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			cstart = str.lower(input("To choose an option, type 'y' or 'n.'\nUser:\\>"))
def ab():
	abstart = str.lower(input("\tYou take the sketchy guy's bus route and it actually works. You get to\nexactly where you need to be. However, he demands you pay him 50 times his\nadvertised price. You tell him that you don't have that amount of money and he\ngives you an option:\nA: You deliver a mysterious package to 'a friend' back in town.\nYou can also:\nB: You offer to trade him a picture of a (your) treasure map via email as well\nas pay him the advertised price, but only if he waits until tomorrow\nC: Make a run for it and hide in the forest.\nWhich do you choose?\n\nUser:\\>"))
	validabstart = False
	while validabstart == False:
		if abstart == "a":
			validabstart = True
			print("OK...\n")
			time.sleep(1.0)
			aba()
		if abstart == "b":
			validabstart = True
			print("Interesting idea...\n")
			time.sleep(1.0)
			abb()
		if abstart == "c":
			validabstart = True
			print("I hope you're fast!\n")
			time.sleep(1.0)
			abc()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			cstart = str.lower(input("Type either 'a,' 'b,' or 'c' to choose an option.\nUser:\\> "))
def aba():
	abastart = str.lower(input("\tYou decide to go deliver the package first in exchange for him driving\nyou to the treasure site. He gives you a package and a drop off location and\nsends you on your way. You get to the dropoff point, knock on the door, but just\nas it opens, several undercover policemen detain you for questioning. They\neventually open the package and find a bomb inside and arrest you.\nYour options are:\nA: You tell them your story and ask them for freedom in exchange for leading them\nto the person whogave you the package.\nB: Bribe one of the police guards with the treasure map\n(you have a picture of it saved anyway)\nC: Try to pick the lock while the guard is not looking\n\nUser:\\>"))
	validabastart = False
	while validabastart == False:
		if abastart == "a":
			validabastart = True
			print("Good idea...\n")
			time.sleep(1.0)
			abaa()
		if abastart == "b":
			validabastart = True
			print("I hope the gaurds here are corrput...\n")
			time.sleep(1.0)
			abab()
		if abastart == "b":
			validabastart = True
			print("Better not get caught!\n")
			time.sleep(1.0)
			abab()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			abastart = str.lower(input("To choose an option, type 'y' or 'n.'\nUser:\\>"))
def abb():
	print("\tHe agrees, but warns you that if you don't show up the next day,\nhe will find you and kill you. You find the treasure and run away.\nYou become super rich but live the rest of your life in fear that he will kill you.\nTHE END")
	exit()
def abc():
	abcstart = str.lower(input("\tYou try to run away but one of the guards shoots you and you die.\nTHE END\nWant to play again? [Y/N]\n\nUser:\\> "))
	validabcstart = False
	while validabcstart == False:
		if abcstart == "y":
			validabcstart = True
			print("Nice to see you again...\n")
			time.sleep(1.0)
			start()
		if abcstart == "n":
			validabcstart = True
			print("Goodbye!\n")
			time.sleep(1.0)
			exit()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			abcstart = str.lower(input("To choose an option, type 'y' or 'n.'\nUser:\\>"))
def abaa():
	print("\tYou lead the police to the shady man when you return the next day and\nthey agree to release you. You then find the treasure.\nTHE END")
	exit()
def abab():
	ababstart = str.lower(input("\tSome guards see you and send you to prison. Bad mistake.\nTHE END\nWant to play again?"))
	validababstart = False
	while validababstart == False:
		if ababstart == "y":
			validababstart = True
			print("Nice to see you again...\n")
			time.sleep(1.0)
			start()
		if ababstart == "n":
			validababstart = True
			print("Goodbye!\n")
			time.sleep(1.0)
			exit()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			ababstart = str.lower(input("To choose an option, type 'y' or 'n.'\nUser:\\>"))
def ba():
	bastart = print("\tYou get lost in the jungle and die.\nTHE END.")
	exit()
def bb():
	bastart = print("\tYou follow the path to the treasure and become rich.\nTHE END.")
	exit()
start()











