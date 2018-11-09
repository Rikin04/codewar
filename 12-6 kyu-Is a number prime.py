#https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
from math import sqrt

def is_prime(num):
	if num < 2:
		return False
	for i in range(2 , int(sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

# def is_prime(num):
#     return num > 1 and not any(num % n == 0 for n in range(2,int(sqrt(num)) + 1))

is_prime(1000)