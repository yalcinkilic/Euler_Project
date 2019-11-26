import math_library
"""
This program solves 5th question of Euler Project
"""

prime_list = []
for i in range(1 , 21):
    if math_library.is_prime(i) == True:
        prime_list.append(i)

exponent_list = []
for element in prime_list:
    for i in range(2 , 21):
        if element ** i > 21:
            exponent_list.append(i - 1)
            break

product = 1
for i in range(len(prime_list)):
    product *= (prime_list[i] ** exponent_list[i])

print("The smallest number which is divisible by 1,2,3 .... ,20 is" , product)
