#https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import re
def increment_string(strng):
	regex_str = '\d$'
	if re.search(regex_str, strng):
		l = list(strng)
		for i in range(len(l) - 1, -1, -1):
			if (i != 0 and re.search('\d', l[i - 1]) and int(l[i]) + 1 == 10):
					l[i] = 0  
			else:
				l[i] = int(l[i]) + 1
				return ''.join(l[0 : i]) + ''.join(str(x) for x in l[i : ])
	return strng + str(1) 
