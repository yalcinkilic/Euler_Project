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
"""
Suppose a number N("number1" below) is divisible by everything 1, 2, 3 , N/3 ,  N/2 . Then ,
sum of all this numbers is equals to N( 1/2 + 1/3 + ... + 1/N) which is at most N * (ln10000)
,i.e less than N*10 . So if M("number2" below) greater than N*8 they cannot form a amicable pair

Further analysis: If M("number2" below) is divisible by 2 , then it cannot be bigger than
N * 2 , if it is not divisible by 2 , then we have at most N(1/3 + 1/5 + ... + 1/N) which is at
less than 5*N by the above logic
"""

start_time = time.time()
#Let's naively check the amicable pairs using get_divisors
total = 0
for num1 in range(1 , 1000):
    for num2 in range(num1 + 1 , 1000):
        #For the explanation of the if statement check above docstring
        if num2 < (10 * num1) and not(num2 % 2 == 0 and num2 > (num1 * 2)) and not(num2 % 2 != 0 and num2 > (num1 * 5)):
            divisor1_list = math_library.get_divisors(num1)
            divisor2_list = math_library.get_divisors(num2)
            sum_divisor1 = sum(divisor1_list) - num1
            sum_divisor2 = sum(divisor2_list) - num2
            if sum_divisor1 == num2 and sum_divisor2 == num1:
                print(num1 , num2)
                total += (num1 + num2)

stop_time = time.time()
print("Sum of all amicable numbers under 1000 is:" , total)
print(stop_time - start_time , "seconds..")
