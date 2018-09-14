print("This program claculates effective temperature accounting for the wind chill")
print("factor given a temperature in Fahrenheit and a wind speed in miles per hour.")
temperature = float(input("Please enter a temperature value in degrees Fahrenheit: "))
validtemp = True
if temperature > 50 or temperature < -50:
	validtemp = False
while validtemp == False:
	if  temperature > 50 or temperature < -50:
		print("Your temperature value must be between -50 and 50")
		temperature = int(input("Please enter a valid temperature: "))
		if not temperature > 50 and not temperature < -50:
			validtemp = True
windspeed = float(input("Please enter a wind speed in miles per hour:"))
validspeed = True
if windspeed > 50 or windspeed < -50:
	validspeed = False
while validspeed == False:
	if not windspeed > 120 and not windspeed < 3:
		print("Your temperature value must be between 3 and 120")
		temperature = int(input("Please enter a valid temperature: "))
		if not windspeed > 120 and not windspeed < 3:
			validspeed = True
answer = 35.74 + 0.6215*temperature + (0.4275*temperature - 35.75)*windspeed**0.16
print("The effective temperature accounting for the wind chill factor with a")
print("temperature of",temperature,"degrees Fahrenheit and a wind speed of")
print(windspeed,"miles per hour is",answer,"degrees Fahrenheit.")