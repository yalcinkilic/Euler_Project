import math_library
"""
This program solves the 13th Question of Euler Project
"""

def read_txt(filename):
    """
    In our filename.txt we have 50 numbers written as one number per line
    So this function returns a list contains this 50 numbers
    """
    file = open(filename)
    number_list = []
    for line in file:
        number = int(line)
        number_list.append(number)

    return number_list


list = read_txt("Problem13_sum.txt")
total = sum(list)
first_ten_digit = math_library.get_first_n_digit(total ,10)

print("First ten digits of the sums is" , first_ten_digit)
