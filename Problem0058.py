import pyprimes

numOfL = 2
num = 1
primes = 0
notPrimes = 1
while True:
	for i in range(4):
		num += numOfL
		if pyprimes.isprime(num):
			primes += 1
		else:
			notPrimes += 1
	if primes/(primes + notPrimes) < 0.1:
		print(numOfL+1)
		break
	numOfL += 2
