import sys

class ShortestPath():
	def __init__(self, v):
		self.V = v
		self.place = [[0 for column in range(v)]
					for row in range(v)]
#print
	def printSol(self, dist):
		print("Path")
		for i in range(self.V):
			print(i, "to", dist[i])
#check min distance and vertex
	def minDistance(self, dist, Set):
		min = sys.maxsize
		for i in range(self.V):
			if dist[i] < min and Set[i] == False:
				min = dist[i]
				min_index = i
		return min_index

	def ShortestPath(self, src):
		dist = [sys.maxsize] * self.V
		dist[src] = 0
		Set = [False] * self.V
		for cout in range(self.V):
			u = self.minDistance(dist, Set)
			Set[u] = True
			for v in range(self.V):
				if self.place[u][v] > 0 and	Set[v] == False and dist[v] > dist[u] + self.place[u][v]:
					dist[v] = dist[u] + self.place[u][v]

		self.printSol(dist)

g = ShortestPath(7)
g.place = place = [[0, 2, 6, 0, 0, 0, 0], 
        [2, 0, 0, 5, 0, 0, 0], 
        [6, 6, 0, 8, 0, 0, 0], 
        [0, 0, 8, 0, 10, 15, 0], 
        [0, 0, 0, 10, 0, 6, 2], 
        [0, 0, 0, 15, 6, 0, 6], 
        [0, 0, 0, 0, 2, 6, 0],
        ];

g.ShortestPath(0)
