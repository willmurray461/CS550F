#Here is a program created to have a brief conversation with the user. 
#Created by William Murray on 9-6-18.
#The 'os' library and included functions were not created by me and is property of its respective owners.
import os
print("Hi! I am cs.py, a program created to have a short converstion with a user.")
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
reason = input("So what made you decide to run me today? ")
print("Well you didn't really need to run me today because you said '",reason,"' I'm a pretty simple program. My creator has other much more interesting programs made in other languages like Processing.")
answer = input("In fact, let me show it to you. Is that OK? [Y/N] ")
if answer == 'y' or answer == 'Y':
	print("Ok, this will take a second")
	os.system("ls -l -a")

