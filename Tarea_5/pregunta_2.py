import numpy.random as rn
import random
from queue import Queue
from math import isqrt,inf

NIL = 0
class BipGraph:
    def __init__(self,m,n):
        self.m = m
        self.n = n
        self.edges = []
        self.adj = [[] for _ in range(m+1)]
    
    def addEdge(self,node1,node2):
        
        self.adj[node1].append(node2)

    def bfs(self):
        Q = Queue()
        for i in range(1, self.m+1):
            if self.pairU[i] == NIL:
                self.dist[i] = 0
                Q.put(i)
            else:
                self.dist[i] = inf

        self.dist[NIL] = inf

        while not Q.empty():
            u = Q.get()
            if self.dist[u] < self.dist[NIL]:
                for v in self.adj[u]:
                    if self.dist[self.pairV[v]] == inf:
                        self.dist[self.pairV[v]] = self.dist[u] + 1
                        Q.put(self.pairV[v])
        return self.dist[NIL] != inf
    

    def dfs(self,u):
        if u != NIL:
            for v in self.adj[u]:
                if self.dist[self.pairV[v]] == self.dist[u] + 1:
                    if self.dfs(self.pairV[v]):
                        self.pairV[v] = u
                        self.pairU[u] = v
                        return True
            self.dist[u] = inf
            return False
        return True

    def hopcroftKarp(self):
        self.pairU = [0 for _ in range(self.m+1)]
        self.pairV = [0 for _ in range(self.n+1)]
        self.dist = [0 for _ in range(self.m+1)]
        result = 0
 
        while self.bfs():
            for u in range(1, self.m+1):
                if self.pairU[u] == NIL and self.dfs(u):
                    result += 1
        return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    #rn.seed(10)
    A = rn.randint(1,50,25)
    A = list(dict.fromkeys(A))
    #A = [1, 2, 3, 4, 5, 11]
    pares = []
    impares = []
    for i in sorted(A):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    print(pares)
    print(impares)
    print(len(impares))
    print(len(pares))
    maxP = max(A)
    g = BipGraph(maxP,maxP)
    for i in pares:
        for j in impares:
            if is_prime(i+j):
                g.addEdge(i,j)
    #print(g.adj)
    print("Número de vertices a eliminar: %d" % g.hopcroftKarp())
