#!/usr/bin/python

import ImageMatrix

class ResizeableImage(ImageMatrix.ImageMatrix):
    def best_seam(self):
        
		dp = {} #Keys are (i, j) tuples and values 
				#are tuples (energy, seam) with energy
				#being the total energy and the seam being
				#a list of coordinates
		
		for j in range(self.height):
			for i in range(self.width):
				if j is 0: #first row
					dp[(i, j)] = (self.energy(i,j), [(i,j)])
				else: #subsequent rows
					if i>0:
						lef = dp[(i-1, j-1)]
					else:
						lef = (10000, None)
					mid = dp[(i, j-1)]
					if i<self.width-1:
						rgt = dp[(i+1, j-1)]
					else:
						rgt = (10000, None)
						
					if lef[0] <= rgt[0] and lef[0] <= mid[0]:
						#left pixel is smallest energy
						dp[(i, j)] = (self.energy(i, j)+lef[0], lef[1]+[(i,j)])
					elif mid[0] <= lef[0] and mid[0] <= rgt[0]:
						#mid pixel is the smallest
						dp[(i, j)] = (self.energy(i, j)+mid[0], mid[1]+[(i,j)])
					else:
						#right pixel is smallest
						dp[(i, j)] = (self.energy(i, j)+rgt[0], rgt[1]+[(i,j)])
		
		#Now find the best seam
		best = None
		seam = []
		for i in range(self.width):
			j = self.height-1
			if best is None or best > dp[(i, j)][0]:
				best = dp[(i, j)][0]
				seam = dp[(i, j)][1]
		
		return seam						
		

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
