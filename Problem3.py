import math_library
"""
This program solves 3rd question of Euler Project
"""

divisor_list = math_library.factorize_integer(600851475143)
for i in range(len(divisor_list) - 1 , -1 , -1):
    if math_library.is_prime(divisor_list[i]) == True:
        print("The largest prime divisor of 600851475143 is" , divisor_list[i])
        break
