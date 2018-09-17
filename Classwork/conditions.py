num1 = eval(input("Pick a number: "))
num2 = eval(input("Pick a second number: "))
if num1 > num2:
	print(num1,"is greater than",num2)
elif num1 == num2:
	print(num1,"and",num2,"are equal")
else:
	print(num2,"is greater than",num1)