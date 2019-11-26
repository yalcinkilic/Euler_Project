for i in range(9000,10000):
	istrue = True
	astr = str(i) + str(2*i)
	for j in range(1,10):
		if str(j) not in astr:
			istrue = False
			break
	if istrue:
		print(astr)