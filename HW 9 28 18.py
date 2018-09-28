import sys
import random

def fib(digits):
	prevdigit = 0
	currentdigit = 1
	tempdigit = 0
	for x in range(0,digits):
		print(str(currentdigit))
		tempdigit = currentdigit
		currentdigit = currentdigit + prevdigit
		prevdigit = tempdigit

def toDecimal(binarynum):
	decimalnum = 0;
	for x in range(0,len(str(binarynum))):
		decimalnum += (2**x)*int(binarynum[len(binarynum)-x-1])
	print(decimalnum)


def toDecimal2(binarynum):
	decimalnum = 0
	digit = 0
	while binarynum >= 1:
		decimalnum += (binarynum%2)*(2**digit)
		binarynum = binarynum//10
		digit += 1
	print(str(decimalnum))


def primes(num):
	nums = [x for x in range(2,num)]
	composites = []
	for i in range(0,len(nums)):
		for j in range(0,len(nums)):
			if nums[i]%nums[j] == 0 and not nums[i] == nums[j] and nums[i] not in composites and nums[j] not in composites:
				composites.append(nums[i])
				break
	nums = [x for x in nums if x not in composites]
	print(nums)


def randsInOrder():
	nums = [random.randrange(1,101) for x in range(0,10)]
	nums = [x for x in nums if not x%3 == 0]
	nums.sort()
	print(nums)


def shuffledRands():
	nums = [x for x in range(1,101)]
	for x in range(0,101):
		nums[random.randrange(0,100)],nums[random.randrange(0,100)] = nums[random.randrange(0,100)],nums[random.randrange(0,100)]
	print(nums)

#randsInOrder()

#shuffledRands()

primes(int(sys.argv[1]))


#toDecimal(sys.argv[1])


#toDecimal2(sys.argv[1])


#fib(sys.argv[1])


