def detect_collisions(balls):
	""" 
	Detect any pairs of balls that are colliding.
	Returns a set of ball_pairs.
	"""

	set_of_collisions = set()
	bins = {}

	#Add the balls into the bins of size = max diameter
	for i in range(len(balls)):
		x = int(balls[i].x / 256)
		y = int(balls[i].y / 256)
		
		if not bins.has_key((x, y)):
			bins[(x, y)] = set()
		
		bins[(x, y)].add(balls[i])
		
	
	#Check balls in bins and adjacent bins for collisions
	for (x, y) in bins.keys():
		for b1 in bins[(x, y)]:
			for xOff in xrange(-1, 2):
				for yOff in xrange(-1, 2):
					if bins.has_key((x+xOff, y+yOff)):
						for b2 in bins[(x+xOff, y+yOff)]:
							if gas.colliding(b1, b2) and b1 != b2:
								set_of_collisions.add(gas.ball_pair(b1, b2))

	return set_of_collisions

import gas
