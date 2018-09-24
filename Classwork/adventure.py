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
					print("Type either 'a,' 'b,' or 'c' to choose an option.")
					a = str.lower(input(("User:\\> ")))
		elif startanswer == "quit":
			exit()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			startanswer = input("Type 'continue' to continue or 'quit' to exit the program.\nUser:\\> ")
def starta():
	astart = str.lower(input("\tYou arrive at the nearest airport which is still 20 miles from where\nthe maptells you to go. You decide that you should try to take a bus\nto yourdestinaiton, but since you don't speak spanish, you take the wrong\nbus andaccidentally get lost. Fortunately, the bus you accidentally take leads\nyou to apopular tourist site where you find a hotel where people speak english."))
def startb():
	validbstartanswer = False
	print("\tSince you were brave enough to take a bus in, you did some research on\nall the busses you needed to take and got to your destination. It's in the\nmiddle of nowhere and the map says as follows:")
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
	while validbstartanswer == False:
		if bstart == "a":
			ba()
		if bstart == "b":
			bb()
		else:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[F")
			bstart = input("Type either 'a,' 'b,' or 'c' to choose an option.\nUser:\\> ")
def startc():
	print("")
startb()











