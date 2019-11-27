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

"""
We are computing divisor list of the same integer over and over again. Lets pre_compute them
and use the list .
"""

start_time = time.time()
#Compute divisor_list of all numbers from 1 to 10000 first
list_of_sum_divisors = [0]
for number in range(1 , 10000) :
    divisor_list = math_library.get_divisors(number)
    list_of_sum_divisors.append(sum(divisor_list) - number)


total = 0
for num1 in range(1 , 10000):
    #Num2 is our amicable pair candidate for num1
    num2 = list_of_sum_divisors[num1]
    if num2 < 10000 and  num1 != num2 and list_of_sum_divisors[num2] == num1 :
        total += (num1 + num2)
stop_time = time.time()
print("Sum of all amicable numbers less than 10000 is" , total//2)
print(stop_time - start_time , "seconds..")
