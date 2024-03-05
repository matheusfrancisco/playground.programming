#!/usr/bin/python

def fib_recursive(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memoize(n):
	
	memo = {0:0, 1:1}
	
	def lookup(n, memo):
		if not memo.has_key(n):
			memo[n] = lookup(n-1, memo) + lookup(n-2, memo)
		return memo[n]	
	
	return lookup(n, memo)
	
	
def fib_bottom_up(n):
	
	fib = [0, 1]
	for i in xrange(2, n+1):
		fib.append(fib[i-1]+fib[i-2])
	
	return(fib[n])

def fib_in_place(n):
	if n is 0:
		return 0
	elif n is 1:
		return 1
	else:
		n0 = 0
		fib = 1
		for i in range(2, n+1):
			m = n0 + fib
			n0 = fib
			fib = m
			
		f.close()
		return fib
			
