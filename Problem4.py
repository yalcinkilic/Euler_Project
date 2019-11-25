import math_library
"""
This program solves 4th question of Euler Project
"""
#Can we fasten the program?


result_list = []
for num1 in range(100 , 1000):
    for num2 in range(100 , 1000):
        product = num1 * num2
        if math_library.is_palindrome(product) == True:
            result_list.append(product)

print("The largest palindrome which can be written as a product of two 3-digit numbers is" ,max(result_list))
