'''
#  Minimum Spanning Tree 

Spanning Tree - A spanning tree is a subset of Graph G, such that all the vertices are connected
using minimum possible number of edges. Hence, a spanning tree does not have cycles and a graph 
may have more than one spanning tree.

Note: A graph can have multiple spanning tree.

Given a weighted, undirected, and connected graph with V vertices and E edges, your task 
is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the
graph. The graph is represented by an adjacency list, where each element adj[i] is a vector 
containing vector of integers. Each vector represents an edge, with the first integer 
denoting the endpoint of the edge and the second integer denoting the weight of the edge.

# Implemented Minimum Spaning tree using Prims algorithm

Example 1:

Input:
3 3
0 1 5
1 2 3
0 2 1

Output:
4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Example 2:

Input:
2 1
0 1 5

Output:
5

'''
class DisjointSet:
    def __init__(self, noOfNodes):
        self.parent = [i for i in range(noOfNodes + 1)]
        self.rank = [0 for _ in range(noOfNodes + 1)]
        self.size = [1 for _ in range(noOfNodes + 1)]
    
    
    def findUltimateParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]
        
        
    # Will make the links-between-nodes using DisjointSet UnionByRank
    def UnionByRank(self, edge):
        firstParent = self.findUltimateParent(edge[0])
        secParent = self.findUltimateParent(edge[1])
        if firstParent == secParent:
            return
        
        if self.rank[firstParent] < self.rank[secParent]:
            self.parent[firstParent] = secParent
            
        elif self.rank[firstParent] > self.rank[secParent]:
            self.parent[secParent] = firstParent
            
        else:
            self.parent[secParent] = firstParent # Taking convention of connecting 2nd parent below to 1st Parent
            self.rank[firstParent] += 1
        
    
def spanningTree(V, adj):
    #code here
    # Kruskal's Algo
    
    adjList_wt = []
    for rows in range(V):
        for i in adj[rows]:
            adjList_wt.append([i[1], (rows, i[0])])
    
    adjList_wt = sorted(adjList_wt, key = lambda x: x[0])
    summ = 0
    disjoint = DisjointSet(V)
    for edge in adjList_wt:
        if disjoint.findUltimateParent(edge[1][0]) != disjoint.findUltimateParent(edge[1][1]):
            disjoint.UnionByRank([edge[1][0], edge[1][1]])
            summ += edge[0]
    return summ
        

if __name__ == "__main__":
    V, E = map(int, input().strip().split())
    adj = [[] for i in range(V)]
    for i in range(E):
        u, v, w = map(int, input().strip().split())
        adj[u].append([v, w])
        adj[v].append([u, w])
    res = spanningTree(V, adj)
    
    print("the sum of the weights of the edges in the Minimum Spanning Tree (MST): ", res)
   
    
