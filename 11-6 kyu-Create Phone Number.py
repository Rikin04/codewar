#https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):
    strN = [str(x) for x in n]
    return ''.join(['(', ''.join(strN[0 : 3]), ')', ' ', ''.join(strN[3 : 6]), '-', ''.join(strN[6 : ])])
