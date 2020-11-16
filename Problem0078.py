import time
import math

#http://www.numbertheory.org/php/partition.html

start = time.time()

rNList = [-1]
parts = [1]
alphaList = [1]

def findAlpha(n):
	if n == 0:
		return 1
	nSqr = math.sqrt(n)
	for r in range(1, int(nSqr)+1):
		if r+1 > len(rNList):
			if 3*math.pow(r, 2) - r > 2 * n:
				break
			rNList.append([3*math.pow(r, 2) + r, 3*math.pow(r, 2) - r])
		if (rNList[r][0] == 2 * n) or (rNList[r][1] == 2 * n):
			return int(math.pow(-1, r))
	return 0

def partitions(n):
	count = 0
	for i in range(1, n+1):
		if i+1 > len(alphaList):
			alpha = findAlpha(i)
			alphaList.append(alpha)
		if alphaList[i] == 1:
			count -= parts[n-i]
		elif alphaList[i] == -1:
			count += parts[n-i]
	parts.append(count)
	return count

n = 1
while True:
	result = partitions(n)
	if result % 1000000 == 0:
		end = time.time()
		print("\n========================================================")
		print("n =", n , "finished in", end - start, "secs")
		print("========================================================")
		break
	if n % 1000 == 0:
		print("n =", n, "is finished")
	n += 1






