#fahrenheit = float(input("This program will convert a temperature in Fahrenheit to Celsius. Enter a value to continue: "))
#answer = (fahrenheit - 32) * 5 / 9
#print(fahrenheit,"degrees Fahrenheit is",answer,"degrees Celsius.")

#import random
#while True:
	#r = random.randrange(0, 101 ,10)
	#print(str(r))

import math
angleD = float(input("Enter a value in degrees: "))
angleR = angleD*360/(2*math.pi)
answer = math.sin(angleR)**2 + math.cos(angleR)**2
print("sin(",angleD,"°)^2 + cos(",angleD,"°)^2 =",answer)
