#Factorial
import sys
def factorial(num):
	if num < 0 or not type(num) == int:
		print("Error.")
		exit()
	if num == 0:
		factorialnum = 1
	else:
		factorialnum = num
		for x in range(1, num-1):
			factorialnum = factorialnum*(num-x)
			sys.stdout.write("\033[F")
			completed = x/num
			print(int(completed*100),"\b% Completed")
	print(factorialnum)
#factorial(1)

def factorial2(num):
	if num == 0 or num == 1:
		return 1
	else:
		return num * factorial2(num-1)
#print(factorial2(1))

def fib(digits):
	prevdigit = 0
	currentdigit = 1
	tempdigit = 0
	for x in range(0,digits-1):
		#print(str(currentdigit))
		tempdigit = currentdigit
		currentdigit = currentdigit + prevdigit
		prevdigit = tempdigit
		completed = x/digits
		sys.stdout.write("\033[F")
		print(int(completed*100),"\b% Completed")
	print(currentdigit)
fib(5)

def fib2(num):
	if num == 0 or num == 1:
		return num
	else:
		return fib(num-1) + fib(num-2)
#print(fib(1))
