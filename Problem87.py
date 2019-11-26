import pyprimes
import itertools
import math
import time

start = time.time()

numList = []

below = 5000000

cUpper = math.ceil(below**(4**-1))
primeList = list(pyprimes.primes(2,math.ceil(math.sqrt(50000000))))
cList = primeList[:pyprimes.prime_count(cUpper-1)]

for i in range(len(cList)-1, -1, -1):
	csquare = cList[i]**4
	bUpper = math.ceil((below-csquare)**(3**-1))
	bList = primeList[:pyprimes.prime_count(bUpper-1)]

	for j in range(len(bList)-1, -1, -1):
		bsquare = bList[j]**3
		aUpper = math.ceil(math.sqrt(below-csquare-bsquare))
		aList = primeList[:pyprimes.prime_count(aUpper-1)]

		for k in range(len(aList)-1, -1, -1):
			result = (aList[k]**2 + bsquare + csquare)			
			if result not in numList:
				numList.append(result)

print(len(numList))

end = time.time()
print(end - start)