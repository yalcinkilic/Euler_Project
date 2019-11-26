import math_library
"""
This program solves 2nd question of Euler Project
"""

fibo_list = math_library.compute_fibonacchi_numbers(4000000)
total = 0
for element in fibo_list:
    if element % 2 == 0:
        total += element

print("The sum of all even fibonacchi numbers less than 4 million is" , total)
