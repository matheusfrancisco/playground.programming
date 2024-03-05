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
	s_substrings = set()
	# Put all substrings of s of length k into a set: s_substrings
	for s_start in range(len(s)-k+1):
		current = s[s_start : s_start+k]
		s_substrings.add(current)
	# For every substring of t of length k, look for it in
	# s_substrings. If it's there, return it.
	for t_start in range(len(t)-k+1):
		current = t[t_start : t_start+k]
		if current in s_substrings:
			return current
	return None
