import timeit
import random

def createSet(n):
	#creates a set with 10^n elements
	s = set()
	for x in xrange(10**n):
		r = random.random()
		while r in s:
			r = random.random()
		s.add(r)
		
	return s
		


if __name__ == '__main__':
	
	for a in xrange(3, 7):
		for b in xrange(3, 7):
			
			print "Testing 10^",a," intersect with 10^",b
			s = createSet(a)
			t = createSet(b)
			
			time = timeit.Timer("s.intersection(t)", "from __main__ import s, t")
			try:
				print "Execution time is: ", time.timeit(100), "\n"
			except:
				time.print_exc()