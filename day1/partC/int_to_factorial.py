import sys


def factorial(n):
	if n == 0:
		return 1
	else:
		fac = n
		while n > 1:
			n = n - 1
			fac *= n
		return fac


#
# NOT WORKING!
# 
def fibonacci(n):
	fib = 0	
	fibSeq = [0, 1]
	while fib < n:
		arg1 = fibSeq[-2]
		arg2 = fibSeq[-1]
		fib = arg1 + arg2
		fibSeq.append(fib)
	return fibSeq

def fibonacci2(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a


integer = int(sys.argv[1])

print factorial(integer)

print fibonacci(integer)

print fibonacci2(integer)
