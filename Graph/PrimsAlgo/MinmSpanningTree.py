'''
#  Minimum Spanning Tree 

Given a weighted, undirected, and connected graph with V vertices and E edges, your task 
is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the
graph. The graph is represented by an adjacency list, where each element adj[i] is a vector 
containing vector of integers. Each vector represents an edge, with the first integer 
denoting the endpoint of the edge and the second integer denoting the weight of the edge.

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

from heapq import *

def spanningTree(V, adj):
    #code here
    visited = [False] * V
    summ = 0
    priorityQ = [(0, 0)]
    
    heapify(priorityQ)
    
    while priorityQ:
        wt, el = heappop(priorityQ) # min heap pop
        if visited[el]:
            continue
        visited[el] = True
        summ += wt
        
        for adjel in adj[el]:
            adjn = adjel[0]
            adjw = adjel[1]
            if not visited[adjn]:
                heappush(priorityQ,(adjw, adjn))
    return summ
    
if __name__ == "__main__":
    # adj = [[[1, 5], [2, 1]], [[2, 3]]]
    # V = 3
    V, E = map(int, input().strip().split())
    adj = [[] for i in range(V)]
    for i in range(E):
        u, v, w = map(int, input().strip().split())
        adj[u].append([v, w])
        adj[v].append([u, w])
    res = spanningTree(V, adj)
    
    print("the sum of the weights of the edges in the Minimum Spanning Tree (MST): ", res)
    
