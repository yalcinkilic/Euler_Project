import math

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

abund = []
for i in range(1, 28124):
	if sum(factorize(i)) > 2 * i:
		abund.append(i)

numbers = [0] * 28124
for i in range(len(abund)):
	for j in range(i,len(abund)):
		summ = abund[i] + abund[j]
		if summ > 28123:
			break
		numbers[summ] = 1

total = 0
for i in range(len(numbers)):
	if numbers[i] == 0:
		total += i

print(total)