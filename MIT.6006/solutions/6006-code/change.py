#!/usr/bin/python

def make_change(denominations, C):
	
	change = {0:[], 1:[1]}

	
	for i in range(2, C+1):
		minimum = None
		coins = []
		for d in denominations:
			if d <= i:
				if minimum is None or minimum > (len(change[i-d])+1):
					minimum = len(change[i-d])+1
					coins = change[i-d]+[d]			
		change[i] = coins
						
	return change[C]
