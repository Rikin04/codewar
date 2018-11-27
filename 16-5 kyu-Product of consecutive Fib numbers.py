def productFib(prod):
    l = [0, 1, False]
    while (l[0] * l[1] != prod):
    	if l[0] * l[1] > prod:
    		return l
    	else:
    		l[0], l[1] = l[1], l[0] + l[1]
    l[-1] = True
    return l


def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]

