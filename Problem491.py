class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

"""
perms = list(perm_unique([0,1]*4))

print(len(perms))
count = 0
count2 = 0

for element in perms:
	summ = 0
	for i in range(8):
		if element[i] == 1:
			summ += i//2

	if summ == 6:
		if element[0] == 1 and element[1] == 1:
			count += 18
		elif element[0] == 1 or element[1] == 1:
			count += 27
		else:
			count += 36

print(count)

"""

perms = list(perm_unique([0,1]*10))

count = 0

for element in perms:
	summ = 0
	for i in range(20):
		if element[i] == 1:
			summ += i//2

	if summ == 67 or summ == 56 or summ == 45 or summ == 34 or summ == 23:
		if element[0] == 1 and element[1] == 1:
			count += 12859560000 * 8 / 10
		elif element[0] == 1 or element[1] == 1:
			count += 12859560000 * 9 / 10
		else:
			count += 12859560000
		
print(count)