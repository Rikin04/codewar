#https://www.codewars.com/kata/valid-braces/train/python

def validBraces(string):
  strL = []
  strDict = {"(": ")", "[": "]", "{": "}"}
  for i in string:
  	if i in strDict.keys():
  		strL.append(strDict[i])
  	else :
  		if len(strL) == 0 or strL[-1] != i:
  			return False
  		del strL[-1]
  return len(strL) == 0
