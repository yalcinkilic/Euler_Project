import math_library
"""
This solves 45th question of Euler Project
"""

is_done = False
exponent = 3
while True:
    hexagonal_numbers = math_library.hexagonal_numbers_list(10 ** exponent)
    pentagonal_numbers = math_library.pentagonal_numbers_list(10 ** exponent * 2)
    for i in range(2 , 10 ** exponent):
        hexagonal_number = hexagonal_numbers[i]
        triangular_number = (2 * i - 1) * 2 * i
        if hexagonal_number in pentagonal_numbers and hexagonal_number != 40755:
            is_done = True
            print(hexagonal_number)
            break
    if is_done == True:
        break
    else:
        exponent += 1
