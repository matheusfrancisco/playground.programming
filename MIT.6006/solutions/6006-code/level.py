import rubik

def positions_at_level(level):
    
	#Implement a BFS rubik.I is the solved position and rubik.quarter_twists are the
	#set of permutations (done using apply_perm) that can transform a given position
	
	positions = [rubik.I]
	oldFrontier = [rubik.I]
	newFrontier = None
	
	
	for lvl in range(level):
		newFrontier = []
		for pos in oldFrontier:
			for perm in rubik.quarter_twists:
				newPos = rubik.perm_apply(perm, pos)
				if not newPos in positions:
					positions.append(newPos)
					newFrontier.append(newPos)
		oldFrontier = newFrontier
		
	if newFrontier == None:
		size = 1
	else:
		size = len(newFrontier)		


	return size
