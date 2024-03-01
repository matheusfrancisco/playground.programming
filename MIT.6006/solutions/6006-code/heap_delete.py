from heap import *

class heap_delete(heap):
	def delete(self, i):
		
		self.decrease_key(i, negative_infinity())
		self.extract_min()
		
		
		

