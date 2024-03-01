import math

def inner_product(L1,L2,domain):
	"""
	Inner product between two vectors, where vectors
	are represented as alphabetically sorted (word,freq) pairs.

	Example: inner_product([["and",3],["of",2],["the",5]],
						   [["and",4],["in",1],["of",1],["this",2]]) = 14.0 
	"""
	sum = 0.0
	i = 0
	j = 0
	while i<len(L1) and j<len(L2):
		# L1[i:] and L2[j:] yet to be processed
		if L1[i][0] == L2[j][0]:
			# both vectors have this word
			if L1[i][0] in domain:
				sum += L1[i][1] * L2[j][1]
			i += 1
			j += 1
		elif L1[i][0] < L2[j][0]:
			# word L1[i][0] is in L1 but not L2
			i += 1
		else:
			# word L2[j][0] is in L2 but not L1
			j += 1
	return sum

def vector_angle(L1,L2):
	"""
	The input is a list of (word,freq) pairs, sorted alphabetically.
	Return the angle between these two vectors.
	"""
	set1 = set()
	for i in L1:
		set1.add(i[0])
	set2 = set()
	for i in L2:
		set2.add(i[0])
	domain = set1.intersection(set2)
	
	numerator = inner_product(L1,L2,domain)
	denominator = math.sqrt(inner_product(L1,L1,domain)*inner_product(L2,L2,domain))
	return math.acos(numerator/denominator)
