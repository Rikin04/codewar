# https://www.codewars.com/kata/55466989aeecab5aac00003e

def sqInRect(lng, wdth):
    l = []
    if lng == wdth:
    	return None
    while(wdth != lng):
    	if(lng < wdth):
    		lng, wdth = wdth, lng
    	l.append(wdth)
    	lng -= wdth
    l.append(wdth)
    return l