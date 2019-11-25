import math_library
import random

for i in range(20):
    random_number = random.randint(1 , 1000)
    str_random_number = str(random_number)
    length = len(str_random_number)
    n = random.randint(1 , length)
    print("The first" , n , "digit of the" , random_number , "is" , math_library.get_first_n_digit(random_number,n))
