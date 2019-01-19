#imports the random function
import random
#imports matplotlib for graphing
import matplotlib.pyplot as plt
#creates a function "learn," which returns the student's random learning speed
def learn(hrs):
	return hrs*random.randrange(400,1000)
#creates a function "sleep," which returns the estimated time it would take
#to complete a test depending on how much rest the student got
def sleep(hrs):
	return (2**(9-hrs)+6)*10
#creates a function "test," which returns a random test size
def test():
	return random.randrange(700,1000)
#creates an array of grades 20000 entries long
grades = [0 for x in range(0,20000)]
#creates an array used to plot the x axis for graphing
r = [x for x in range(1,121)]
#loops 20000 times:
for x in range(0,20000):
	#sets hours of sleep
	sleephrs = 8.25
	#sets hours of studying according to sleeping
	studyhrs = 11 - sleephrs
	#student "learns"
	contentlearned = learn(studyhrs)
	#test is "written"
	testcontent = test()
	#if the student finishes studying early, the student goes to sleep
	if contentlearned > testcontent:
		sleephrs += (contentlearned/studyhrs)/testcontent-1
		contentlearned = testcontent
	#sets the time it will take the student to finish the test with the amount of rest they got
	completiontime = sleep(sleephrs)
	#records the approximated grade
	grade = int((contentlearned/testcontent)*(70/completiontime)*100)
	#adds the grade to the list of grades
	grades[x] = grade
	#prints the grade
	print(grade)
#prints the average grade
print("")
print(sum(grades)/len(grades))
#sorts the grades from least to greatest
grades.sort()
#creates an array used to lot the y axis for graphing 
display = [0 for i in range(0,120)]
#transfers the grades to the graph
for i in range(0,2000):
	display[grades[i]] += 1
#displays the graph
plt.plot(r,display)
plt.ylabel("Frequency of grade")
plt.xlabel("Grade")
plt.show()

