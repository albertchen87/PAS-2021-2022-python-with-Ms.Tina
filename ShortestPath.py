import sys
import random

class board():

    def __init__(self, n):
        self.V = n
        self.board = [[0 for column in range(n)]
                    for row in range(n)]

    def printSolution(self, dist):
        for node in range(self.V):
            print("from", node, "to", dist[node])

    def minDistance(self, dist, sptSet):

        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def find(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.board[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.board[u][v]:
                    dist[v] = dist[u] + self.board[u][v]

        self.printSolution(dist)

n = 8

g = board(n)
blah = [[0 for column in range(n)]
                    for row in range(n)]


for i in range(n):
    for j in range(n):
        blah[i][j] = int(random.random()*n)

g.board = blah
print(g.board)


g.find(0)