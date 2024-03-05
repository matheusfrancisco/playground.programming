import bstsize

class BST(bstsize.BST):
	"""
	Adds select method to BST, starting with code from bstsize.	  
	"""
	
	def select(self, index):
		"""
		Takes a 1-based index, and returns the element at that index,
		or None if the index is out-of-bounds.

		Implementation:
		
			The algorithm first initializes rank to be the size of
		the root's left-child BST. From there rank is manipulated after
		a series of left or right traversals. Traversals are based on:
		
			index < rank => go left
			index > rank => go right
			index = rank => stop, return element
			
			The rank is adjusted as follows:
			
			A left traversal subtracts the size of its right-child's BST
		and another 1 from the parent's rank.
		
			A right traversal adds the size of its left-child's BST and 1
		from the parent's rank.
		
		"""
		node = self.root
		elem = None
		
		#initialize rank
		if node.left is not None:
			rank = bstsize.size(node.left) + 1
		else:
			rank = 1
		
		while node is not None and elem is None:
			if index == rank:
				elem = node
				
			elif index < rank:
				if node.left is not None:
					#traverse left
					node = node.left
					if node.right is None:
						rsize = 0
					else:
						rsize = bstsize.size(node.right)
					rank = rank - rsize - 1
				else:
					#left traversal impossible, index out of range
					node = None
					
			else: #index > rank
				if node.right is not None:
					#traverse right
					node = node.right
					if node.left is None:
						lsize = 0
					else:
						lsize = bstsize.size(node.left)
					rank = rank + lsize + 1
				else:
					#right traversal impossible index out of range
					node = None
			
		
		
		return elem
