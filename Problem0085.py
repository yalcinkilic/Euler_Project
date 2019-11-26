import math
diff = 1000000007
closeA = 0
closeB = 0

for a in range(1,2001):
	upperbound = math.ceil(math.sqrt(8000000/(math.pow(a,2))))
	for b in range(upperbound, 1, -1):
		numOfGrids = (b+1)*(a+1)*a*b
		if abs(numOfGrids - 8000000) < diff:
			closeA = a
			closeB = b
			diff = abs(numOfGrids - 8000000)
		if numOfGrids < 8000000:
			break

print("a is: ", closeA)
print("b is: ", closeB)
print("area is: ", closeA*closeB)
print("# of grids is: ", (closeB+1)*(closeA+1)*closeA*closeB/4)