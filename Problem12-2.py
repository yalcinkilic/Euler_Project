import math

def printDict(myDict):
	for i in myDict:
		print(i, "-->", len(myDict[i]))

def factorize(num):
	factors = []
	for j in range(1,int(math.sqrt(num))+1):
		if num % j == 0:
			factors.append(j)
	listLength = len(factors)
	for j in range(listLength):
		result = num//factors[listLength-j-1]
		if result != factors[listLength-j-1]:
			factors.append(result)
	return factors

factors = {}

for i in range(10000,10000):
	triangle = i * (i+1) // 2
	factors[triangle] = factorize(triangle)
	if len(factors[triangle]) >= 500:
		break

printDict(factors)