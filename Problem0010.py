import math_library
"""
This solves 10th Question of Euler Project
"""
total = 0
for i in range(1 , 2000000):
    if math_library.is_prime(i) == True:
        total += i

print("Sum of all primes below 2 million is" , total)
