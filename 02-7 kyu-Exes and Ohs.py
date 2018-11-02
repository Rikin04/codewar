#https://www.codewars.com/kata/exes-and-ohs/train/python

def xo(s):
	s = s.lower()
	return s.count('x') == s.count('o')