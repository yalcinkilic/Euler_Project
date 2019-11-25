"""
This library defines some useful functions using an useless implementation
to solve Euler project questions
"""
import random
import time
import math
"""
25.11.2019 known problems or questions or planned extensions or etc. :
(a) greatest_common_divisor function is a recursive one , should we change it to
a iterative version?
(b) should we add timer to all functions?
(c) should we do some testing for all functions?
(d) should we convert factorize_integer to a iterative function?
(e) add docstring for last 5 functions
(f) check performance of the functions
"""

def greatest_common_divisor(num1 , num2):
    """
    This function computes the greatest common divisor of two numbers.
    Assumptions: The given numbers are positive integers
    Arguments:
    i)  "num1" : Int , first number
    ii) "num2" : Int , second number
    Return value:
    i) "gcd" : Int , greatest common divisor of given two numbers.
    Known Bugs: None
    """
    #Assume that first number is the bigger number otherwise swap them
    if num1 < num2 :
        temp = num2
        num2 = num1
        num1 = temp

    #Initialize the algorithm
    divisor = num1 // num2
    remainder = num1 - num2 * divisor
    if remainder == 0:
        stop_time = time.time()
        return num2
    else:
        return greatest_common_divisor(num2 , remainder)

def solve_linear_diaphtine(first_coefficient , second_coefficient , constant):
    """
    This function solves ax + by = c where gcd(a,b) = 1
    """
    pass

def is_prime(number):
    """
    This function checks whether "number" is prime or not.
    Assumptions: The given number is really an integer
    Arguments:
    (i) "number" : An integer , which we want to check whether it is a prime or not
    Return value:
    (i) boolean : True  -> indicating that "number" is prime
                  False -> indicating that "number" is composite
    Known Bugs: None
    """
    #Handle some special cases
    if number <= 1:
        return False

    #Below three special cases are written to make the code faster somehow!?
    if number % 2 == 0 :
        return number == 2

    if number % 3 == 0 :
        return number == 3

    if number % 5 == 0 :
        return number == 5

    #Otherwise check all the possible divisors of "number" from 7 to square root of "number"
    #Also the step size is 2 since we know that no even number can divide "number" since
    #"number" cannot be even at this point.
    square_root = int(math.sqrt(number))
    for i in range(7 , square_root + 1 , 2):
        if number % i == 0:
            return False

    return True

def generate_prime(number):
    """
    This function generates first "number" primes
    In other words, if "number" = 5 , the function returns first 5 primes
    Assumptions: The given number is really an integer
    Arguments:
    (i) "number" : An integer , which how many smallest prime numbers we wants
    If "number" = 5 , we get 5 smallest (or first) primes
    Return value:
    (i) "prime_list" : integer list ,which contains first "number" primes
    Known Bugs: None
    """
    #Initialize the count and our list
    count = 0
    start = 2
    prime_list = []

    #Until we have "number" primes search for them
    while count < number:
        #Checkout Bertrand's Postulate for the following loop
        for num in range(start , 2 * start):
            if is_prime(num) == True:
                prime_list.append(num)
                start = num + 1
                break

        count += 1

    return prime_list

def factorize_integer(number):
    """
    This function factorizes "number"
    Assumptions: "number" is really an integer
    Arguments:
    (i) "number" : An integer , which we want to factorizes
    Return value:
    (i) "prime_factors" : integer list , which contains prime factors of "number"
    Known Bugs: None
    """
    #Initialize the prime_factors list
    prime_factors = []

    #Consider all the numbers from 2 to "number" + 1 and check whether they
    #divide "number" or not. It only gives prime factors! Think about it...
    for prime_divisor in range(2 , number + 1):
        if number % prime_divisor == 0 :
            prime_factors.append(prime_divisor)
            return  divisor_list + factorize_integer(number // prime_divisor)
    return prime_factors

def get_divisors(num):
    """
    Get divisors of a particular number
    """
    divisor_list = []
    for divisor in range(1 , (num + 2)//2):
        if num % divisor == 0:
            divisor_list.append(divisor)
    divisor_list.append(num)
    return divisor_list

def compute_fibonacchi_numbers(upper_bound):
    """
    This function all the fibonacchi numbers less than a given number
    """
    fibonacchi_list = [1 , 1]
    pre_fibonacchi = 1
    pre_pre_fibobacchi = 1
    current_fibonacchi = 2
    while current_fibonacchi <= upper_bound:
        fibonacchi_list.append(current_fibonacchi)
        pre_pre_fibobacchi = pre_fibonacchi
        pre_fibonacchi = current_fibonacchi
        current_fibonacchi = pre_fibonacchi + pre_pre_fibobacchi


    return fibonacchi_list


def is_palindrome(number):
    """
    This function checks whether a particular number is is_palindrome or not
    """
    str_number = str(number)
    for i in range(len(str_number)):
        if str_number[i] != str_number[-1 * i - 1]:
            return False
    return True


def get_first_n_digit(number , n):
    """
    This function gets first n digit of the number
    """

    number_of_digits = len(str(number))
    if number_of_digits > n:
        first_n_digits_with_zeros = number % (10 ** (number_of_digits - n))
        first_n_digits_without_zeros = (number - first_n_digits_with_zeros) // (10**(number_of_digits-n))
        return first_n_digits_without_zeros
    else:
        return number
    pass
def get_last_n_digit(number , n):
    """
    This function gets last n digit of the number
    """
    last_digits = number % (10 ** n)
    str_last_digits = str(last_digits)
    #If the length is not enough there must be some zeros at the beginning put them!
    if len(str_last_digits) != n:
        number_of_zeros_required = n - len(str_last_digits)
        str_last_digits = "0" * number_of_zeros_required
        str_last_digits += str(last_digits)

    return str_last_digits
