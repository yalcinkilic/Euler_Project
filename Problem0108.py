import pyprimes as pr
import math

def factors(num):
	result = []
	for i in range(2, math.ceil(math.sqrt(num))):
		if num % i == 0:
			result.append(i)

	return result

num = 1000
mainList = []
main = [num]
subList = [main]
mainList.append(subList)

row = 0
goOn = True

while goOn:
	goOn = False
	subList = []
	for divList in mainList[row]:
		for divisor in divList: 
			if not pr.isprime(divisor):
				baseDivList = divList.copy()
				baseDivList.remove(divisor)
				goOn = True
				factorList = factors(divisor)
				for factor in factorList:
					newDivList = baseDivList.copy()
					newDivList += [factor, divisor//factor]
					if sorted(newDivList) not in subList:
						subList.append(sorted(newDivList))
	if len(subList) > 0:
		mainList.append(subList)		
	if goOn:
		row += 1

for element in mainList:
	print(element)
