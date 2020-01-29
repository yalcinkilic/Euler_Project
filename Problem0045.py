import math_library
"""
This solves 45th question of Euler Project
"""
"""
is_done = False
exponent = 3
while True:
    hexagonal_numbers = math_library.hexagonal_numbers_list(10 ** exponent)
    pentagonal_numbers = math_library.pentagonal_numbers_list(10 ** exponent * 2)
    for i in range(2 , 10 ** exponent):
        hexagonal_number = hexagonal_numbers[i]
        triangular_number = (2 * i - 1) * 2 * i
        if hexagonal_number in pentagonal_numbers and hexagonal_number != 40755:
            is_done = True
            print(hexagonal_number)
            break
    if is_done == True:
        break
    else:
        exponent += 1
"""

import math

"""
every hexagonal number is a triangular number
just go over all hexagonal numbers and check if the number is pentagonal
it can be done by checking if the equation n(3n-1)/2=num has an integral solution
3n^2 - n - 2num = 0
for which the positive root is given by (1 + sqrt(1 + 24 * num)) / 6
"""

def isPentagonal(x):
    root = (1 + math.sqrt(1 + 24 * x)) / 6
    return root.is_integer()

done = False
n = 144 # because 40755 is the 143th hexagonal number
while not done:
    num = n * (2 * n - 1) # nth hexagonal number
    if isPentagonal(num):
        print(num)
        done = True
    n += 1