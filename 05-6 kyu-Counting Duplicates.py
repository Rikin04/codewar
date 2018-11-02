# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    # Your code goes here
    text = text.upper()
    count = 0
    textDict = []
    for i in text:
    	if i not in textDict and text.count(i) > 1:
    		textDict.append(i)
    		count += 1
    return count