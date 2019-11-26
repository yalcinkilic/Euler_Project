
#Result is ===> Number_of_partition(100) - 1

def printList(mylist):
	for i in range(1,len(mylist)+1):
		print(i,"-->",mylist[i-1])

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

numOfDigits = 50
num = [1] * numOfDigits
parts = [num]
last = 0
while True:
	length = len(parts)
	for k in range(last, length):
		start = 0
		for i in range(2,numOfDigits):
			if start + i <= numOfDigits:
				toBeAdded = [sum(parts[k][start:start+i])]
				new = sorted(toBeAdded + parts[k][start+i:])
				if new not in parts and len(new) != 1:
					parts.append(new)
					print(new)
			else:
				break
	last = length
	if len(parts) == last:
		break
"""
def partition(number):
	answer = set()
	answer.add((number, ))
	for x in range(1, number):
		for y in partition(number - x):
			answer.add(tuple(sorted((x, ) + y)))
	return len(answer)

print(partition(100))
"""


"""

parts = {}
part = "11"
parts[1] = [part]

for i in range(2,100):
	parts[i] = []
	length = len(parts[i-1])
	for j in range(length):
		new = ''.join(sorted(parts[i-1][j] + "1"))
		if new not in parts[i]:
			parts[i].append(new)
	for j in range(length):
		for k in range(9):
			new = ''.join(sorted(parts[i-1][j]))
			digit = str(k)
			if digit in new:
				index = new.find(digit)
				new = ''.join(sorted(new[:index] + str(int(new[index]) + 1) + new[index+1:]))
				if new not in parts[i]:
					parts[i].append(new)
	print(i+1, '-->', len(parts[i]))	
"""
