import math_library
import time
"""
This solves 21st question of Euler Project

PROBLEM : Extremely naive approach works in 20 seconds even for the amicable numbers
between 1 and 1000. Thus , (much) better method is required... Also it is not hard to
guess that amicable numbers are very rare. Thus there must be a better way to search
for them.
QUESTION : Maybe is_amicable function can be written in math_library ?
"""
start_time = time.time()
#Let's naively check the amicable pairs using get_divisors
total = 0
for num1 in range(1 , 1000):
    for num2 in range(num1 , 1000):
        divisor1_list = math_library.get_divisors(num1)
        divisor2_list = math_library.get_divisors(num2)
        sum_divisor1 = sum(divisor1_list) - num1
        sum_divisor2 = sum(divisor2_list) - num2
        if sum_divisor1 == num2 and sum_divisor2 == num1 and num1 != num2:
            print(num1 , num2)
            total += (num1 + num2)

stop_time = time.time()
print("Sum of all amicable numbers under 1000 is:" , total * 2)
print(stop_time - start_time , "seconds..")
