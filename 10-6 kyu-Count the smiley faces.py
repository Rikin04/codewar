#https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

import re
def count_smileys(arr):
	return len(re.findall(r'[:;][-~]?[D)]',' '.join(arr)))
