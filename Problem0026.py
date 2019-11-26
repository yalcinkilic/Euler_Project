maxcount = 0
for i in range(1,1000):
	remainderList = []
	remainder = "10"
	count = 0
	while True:
		a = 0
		while i > int(remainder):
			remainder += "0"
			if a > 0:
				count += 1
			a += 1
		if remainder in remainderList:
			break
		remainderList.append(remainder)
		remainder = str(int(remainder) % i)
		count += 1
		if remainder == "0":
			break
	if maxcount < count:
		maxcount = count
		maxnumber = i
print(maxcount)
print(maxnumber)