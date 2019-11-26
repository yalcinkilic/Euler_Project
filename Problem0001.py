"""
This program solves the first question of Euler Project
"""

total = 0
for num in range(1 , 1000):
    if num % 5 == 0 or num % 3 == 0:
        total += num

print("The sum of all numbers which are divisible by 3 or 5 below 1000 is" , total)
