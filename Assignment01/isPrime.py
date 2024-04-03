"""
Name: Aayog Koirala
Date: Jan 14, 2020
Desc: Is Prime: Checks if the input number is prime or not
"""

from math import sqrt


def check_prime(n):
    count = 0
    if n <= 1:
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            count += 1

    if count == 0:
        return True
    else:
        return False


num = int(input("Enter your number:"))
isPrime = check_prime(num)
if isPrime:
    print(f"{num} is prime!")
else:
    print(f"{num} is not prime.")
