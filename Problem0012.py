import math_library
import time
"""
This program solves 12th question of Euler Project
MAIN IDEA = Suppose f(NUM) := number of divisors of NUM
f(NUM) = f(divisor1) * f(divisor2) assuming that
(i)  divisor1 * divisor2 = NUM and
(ii) gcd(divisor1 , divisor2) = 1
"""
#Lets look at the timing
start_time = time.time()

#Initialize the number
n  = 1
number = n * (n + 1) // 2

#Until we get the smallest triangular number which has 500(lets call it D) divisors continue searching
#By the way can we prove that this algorithm even stops for any D????
while True:
    #If n is even
    if n % 2 == 0 :
        k = n // 2
        divisor_list = math_library.get_divisors(k)
        divisor_list2 = math_library.get_divisors(n+1)
        #For the following line check out the main idea
        if len(divisor_list) * len(divisor_list2) >= 500:
            print("First triangular number which has more than 500 divisors is" , number)
            stop_time = time.time()
            print("Total time takes is" , stop_time-start_time , "seconds.")
            break
    #If n+1 is even, i.e n is odd:)
    else:
        k = (n+1) // 2
        divisor_list = math_library.get_divisors(k)
        divisor_list2 = math_library.get_divisors(n)
        #For the following line check out the main idea
        if len(divisor_list) * len(divisor_list2) >= 500:
            print("First triangular number which has more than 500 divisors is" , number)
            stop_time = time.time()
            print("Total time takes is" , stop_time-start_time , "seconds.")
            break

    n += 1
    number = n * (n + 1) // 2
