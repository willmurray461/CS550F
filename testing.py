import sys
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


def Primes(num):
	nums = [x for x in range(2,num)]
	primes = []
	composites = []
	for i in range(0,len(nums)-1):
		for j in range(0,len(nums)-1):
			z = nums[i] % nums[j]
			if z == 0 and not nums[i] == nums[j]:
				composites.append(nums[i])
	primes = [x for x in nums if x not in composites]
	print(primes)


Primes(25)


#toDecimal(sys.argv[1])


#toDecimal2(sys.argv[1])


#fib(sys.argv[1])


