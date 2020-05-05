import pyprimes as pr
import math

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	while(first<=last):
		mid = (first + last)//2
		if item_list[mid] == item :
			return mid
		elif mid < len(item_list)-1 and item_list[mid] < item and item_list[mid+1] > item:
			return mid
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	

highest = 10**8
#primesBelow = list(pr.primes_below(math.sqrt(highest)))
primesBelow2 = list(pr.primes_below(highest/1.99))
primesBelow = primesBelow2[:binary_search(primesBelow2, math.sqrt(highest))+1]

count = 0
for i in range(len(primesBelow)):
	prime1 = primesBelow[i]
	div = (highest/prime1)//1
	count += binary_search(primesBelow2, div) - binary_search(primesBelow, prime1) + 1

print(count)
