#https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

import math
def zeros(n):
	count = 0
	while(n != 0):
		n = math.floor(n / 5)
		count += n
	return count

print(zeros(125))