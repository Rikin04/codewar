#https://www.codewars.com/kata/are-the-numbers-in-order/train/python
def in_asc_order(arr):
    # random_ is not allowed
    return arr == sorted(arr)