import heap_id
import re
import math

def node_by_name(nodes, city, state):
	for node in nodes:
		if state == node.state:
			match = re.search(city, node.description)
			if match:
				return node
	return None

def distance(node1, node2):
	return math.hypot(node1.latitude-node2.latitude, node1.longitude-node2.longitude)

def shortest_path(nodes, edges, weight, s, t):
	
	G = Graph(nodes, edges, s)
	(key, ID) = G.queue.extract_min_with_id()
	u = G.nodes[ID]
	while u != t:
		
		for edge in G.edges[u]:
			if u is edge.begin:
				out = edge.end
			else:
				out = edge.begin
			G.relax(u, out, weight)
			
		(key, ID) = G.queue.extract_min_with_id()
		u = G.nodes[ID]
	
	return G.paths[t]

class Graph:
	
	def __init__(self, nodes, edges, s):
		self.queue = heap_id.heap_id()
		self.nodes = {}
		self.costs = {}
		self.paths = {}
		self.IDs = {}
		
		#Insert all of the nodes
		for node in nodes:
			if node == s:
				ID = self.queue.insert(0)
				self.paths[node] = [s]
				self.costs[node] = 0
			else:
				ID = self.queue.insert(heap_id.positive_infinity())
				self.paths[node] = None
				self.costs[node] = heap_id.positive_infinity()
			self.nodes[ID] = node
			self.IDs[node] = ID
	
		#Add all edges to an adjacency list
		self.edges = {}
		for edge in edges:
			if not self.edges.has_key(edge.begin):
				self.edges[edge.begin] = [edge]
			else:
				self.edges[edge.begin].append(edge)
			if not self.edges.has_key(edge.end):
				self.edges[edge.end] = [edge]
			else:
				self.edges[edge.end].append(edge)	
		
	def relax(self, v1, v2, weight):
		
		if self.costs[v2] > (self.costs[v1] + weight(v1, v2)):
			self.costs[v2] = self.costs[v1] + weight(v1, v2)
			self.paths[v2] = self.paths[v1] + [v2]
			self.queue.decrease_key_using_id(self.IDs[v2], self.costs[v2])
			
			
	