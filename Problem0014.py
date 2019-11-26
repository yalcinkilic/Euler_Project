"""
Solves 14th problem of Euler
"""

def collatz_sequence(number):
    """
    Construct collatz sequence of a given number
    """
    step = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number *= 3
            number += 1
        step += 1
    return step

max_step = 0
max_number = 1
for num in range(1 , 1000000):
    step = collatz_sequence(num)
    if step > max_step :
        max_step = step
        max_number = num
print(max_number)
