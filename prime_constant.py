# prime_constant.py
# Andrew Lounsbury
# 19/3/23
# Purpose: Compute the constant discussed in this (https://www.youtube.com/watch?v=_gCKX6VMvmU) video
import math

def prime(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sequence = []
for n in range(1, 100000000):
    # loop through the numbers less than n
    for i in range(2, 1000000):
        # if prime and doesn't divide n, add it to the sequence and move to the next number 
        if prime(i) and n % i != 0:
            sequence.append(i)
            break
total = 0
for x in sequence:
    total += x

average = total / len(sequence)
print("average:", average)