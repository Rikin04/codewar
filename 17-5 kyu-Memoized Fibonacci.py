#https://www.codewars.com/kata/529adbf7533b761c560004e5/train/python

l = [0, 1]
def fibonacci(n):
	if n < len(l):
		return l[n]
	l.append(fibonacci(n - 1) + fibonacci(n - 2))
	return l[-1]

print(fibonacci(70))