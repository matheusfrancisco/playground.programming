import rubik

def shortest_path(start, end):
    
	left = RubikBFS(start)
	right = RubikBFS(end)
	joint = None
	
	f = open('debug.txt', 'w')
	
	if start is end:
		#Start position *is* end position
		return []
	
	else:
		#Step through the BFS from both ends
		steps = 0
		while steps < 8 or joint is None:
			f.write(str(steps)+'\n')
			steps += 1
			joint = left.step(right.tree)
			if joint is None:
				joint = right.step(left.tree)
		
	if joint is not None:			
		moves = left.moves(joint, True) + [joint] + right.moves(joint, False)
	else:
		moves = None

	f.close()

	return moves

class RubikBFS():
	
	def __init__(self, start):
		self.tree = {start:None}
		self.frontier = [start]
		
	def moves(self, joint, flip):
		
		moves = []
		while joint in self.tree.keys():
			moves.append(self.tree[joint])
			joint = self.tree[joint]
		
		if flip:
			moves = moves[-1:-len(moves)]
			
		return moves
		
	def step(self, otherTree):
		#Steps one level through the rubik positions, returns the
		#joint-position if there is a bridge between the two,
		#returns None otherwise
		
		newFront = []
		
		for pos in self.frontier:
			for perm in rubik.quarter_twists:
				newPos = rubik.perm_apply(perm, pos)
				if not newPos in self.tree.keys():
					#Unexplored position
					if newPos in otherTree.keys():
						#joint-position found!
						return newPos
					else:
						self.tree[newPos] = pos
						newFront.append(newPos)
		
		self.frontier = newFront
		
		return None
				
			
		