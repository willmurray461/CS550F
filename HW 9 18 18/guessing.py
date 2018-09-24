# import random
# num = random.randrange(0, 11, 1)
# guess = int(input("Try to guess my number. It is between 0 and 10: "))
# guessed = False
# while guessed == False:
# 	if guess > num:
# 		guess = int(input("Too large. Try again: "))
# 	if guess < num:
# 		guess = int(input("Too small. Try again: "))
# 	if guess == num:
# 		print("You guessed my number.")
# 		guessed = True
validanswer = False
while validanswer == False:
	try:
		num = int(input("Enter a number between 1 and 5, inclusive. "))
	except ValueError:
		print("Hey! That's not a number!")
		num = int(input("Enter a number between 1 and 5, inclusive. "))
	if type(num) == int:
		if not 1 <= num <= 5:
			print("Hey! Out of range.")
	else:
		validanswer = True
print("success")