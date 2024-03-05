def longest_substring(s, t):
	"""Finds the longest substring that occurs in both s and t"""
	best = ''
	
	lo = 0
	hi = min(len(s), len(t))
	
	while lo+1 < hi:
		k = int((lo + hi)/2)
		test = k_substring(s, t, k)
		if test != None:
			lo = k
			best = test
		else:
			hi = k
	
	if lo == hi-1:
		test = k_substring(s, t, hi)
		if test != None:
			best = test	
	
			
	return best

def k_substring(s, t, k):
	"""Finds a substring of length k in both s and t if there is one,
	and returns it. Otherwise, returns None."""
	
	hashS = Hash(s[0:k])
	hashT = Hash(t[0:k])
	
	for sPos in range(0, len(s)-k):
		for tPos in range(0, len(t)-k):
			if hashS.get() == hashT.get():
				if s[sPos:sPos+k] == t[tPos:tPos+k]:
					return s[sPos:sPos+k]
			hashT.skip(t[tPos])
			hashT.append(t[tPos+k])
		hashS.skip(s[sPos])
		hashS.append(s[sPos+k])	
	
	return None
	
	
class Hash():
	
	def __init__(self, s):
		#creates a new hash-object with the given string
		
		self.a = 256
		self.p = 49157 #large prime number chosen to reduce collision frequency		
		self.length = len(s)
		self.aPower = self.a**(self.length-1)
		self.u = 0
		
		for m in xrange(self.length):
			self.append(s[m])
		
	def append(self, c):
		#right-shifts the current hash number by 1 digit and appends character c
		self.u = ((self.u * self.a) + ord(c)) % self.p
	
	def skip(self, c):
		#removes the highest-order bit from the hash number	
		self.u = (self.u - ord(c)*self.aPower%self.p) % self.p
		
	def get(self):
		return(self.u)