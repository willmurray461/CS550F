import os #credit to creators of os library
print("Hi! I am cs.py, a program created to have a short converstion with a user. Before you run me, make sure that you didn't change anything inside this folder where this program is located.")
userName = input("What is your name? ")
print("Nice to meet you,",userName,"\b!\nSo,",userName,"\b,", end = '')
favoriteColor = input(" what's your favorite color? ")
if favoriteColor == "blue" or favoriteColor == "Blue":
	print("Mine is too!")
else:
	print("I don't like",favoriteColor,"that much, my favorite is blue.")
favoriteLanguage = input("What about your favorite programming language? ")
if favoriteLanguage == 'python' or favoriteLanguage == 'Python':
	print("Mine is also! I was programmed in Python.")
else:
	print(favoriteLanguage,"is a great language, but I enjoy Python the most. I was programmed in Python")
favoriteFood = input("What about your favorite food? ")
if favoriteFood == 'pizza' or favoriteFood == 'Pizza':
	print("I hear pizza is great, however I've never had food as I am only a computer program.")
else:
	print("I'm sad because I've never had food. I can't because I'm only a tiny program.")
reason = input("So what made you decide to run me today? ")
print("That's cool. I'm a pretty simple program though. I'm not very interesting. My creator has other much more interesting programs like a recreation/modificaiton of the game 'Spacewar!' he made in Processing.")
answer = input("In fact, let me show it to you. Is that OK? [Y/N] ")
if answer == 'y' or answer == 'Y':
	os.system("open ~/Desktop/'Homework #1'/.Spacewar/Spacewar.pde")
else:
	answer2 = input("I promise it will be cool. :) [Y/N]")
	if answer2 == 'Y' or answer2 =='y':
		os.system("open /'.untitled folder'/Mystery/Mystery.pde")
	else:
		print("OK then. By for now!")
		os.system("exit")


