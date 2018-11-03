#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def find_short(s):
    # your code here
    return min(len(x) for x in s.split())
