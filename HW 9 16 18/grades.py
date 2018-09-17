# THIS IS THE SLOW, BAD WAY TO DO THIS:
# import sys
# a = float(sys.argv[1])
# if 0 <= a <= 5:
# 	if a < 1.0:
# 		print("F")
# 	elif a < 1.5:
# 		print("D-")
# 	elif a < 2.0:
# 		print("D")
# 	elif a < 2.5:
# 		print("D+")
# 	elif a < 2.85:
# 		print("C-")
# 	elif a < 3.2:
# 		print("C")
# 	elif a < 3.5:
# 		print("C+")
# 	elif a < 3.85:
# 		print("B-")
# 	elif a < 4.2:
# 		print("B")
# 	elif a < 4.5:
# 		print("B+")
# 	elif a < 4.7:
# 		print("A-")
# 	elif a < 4.85:
# 		print("A")
# 	else:
# 		print("A+")
# else:
# 	print("number must be between 0 and 5, inclusive")
# 	exit()
# THIS IS THE BETTER, FASTER WAY TO DO THIS:
import sys
userinput = float(sys.argv[1])
if not 0 <= userinput <= 5:
	print("number must be between 0 and 5, inclusive")
	exit()
numbers = [1.0, 1.5, 2.0, 2.5 ,2.85, 3.2, 3.5, 3.85, 4.2, 4.5, 4.7, 4.85, 5.1]
grades = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]
for i in range(0, len(grades)):
	if userinput < numbers[i]:
		print(grades[i])
		break















