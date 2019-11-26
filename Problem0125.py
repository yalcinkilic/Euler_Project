def is_palindrome(number):
	str_number = str(number)
	return str_number == str_number[ : : -1 ]


total = 0

my_list = []

for k in range(1 , 1000):
	for n in range(1,10000):
		result = ((k + 1) * (6 * n * ( n + k ) + k * ( 2*k + 1))) / 6
		result = int(result)
		if is_palindrome(result) == True and result < 100000000 and result not in my_list:
			my_list.append(result)


print(sum(my_list))
