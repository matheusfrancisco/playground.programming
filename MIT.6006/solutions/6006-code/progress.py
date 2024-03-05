#!/usr/bin/python

def longest_increasing_subsequence(scores):
	
	q = [[] for a in range(len(scores))]
	for i in range(len(scores)):
		big = []
		for j in range(i):
			if scores[j] < scores[i]:
				if len(q[j]) > len(big):
					big = q[j]
		q[i] = big + [scores[i]]
	
	big = []
	for i in range(len(scores)):
		if len(q[i]) > len(big):
			big = q[i]
			
	return big
		
