'''
# 1584. Minimum Cost Connect Points


You are given an array points representing integer coordinates of some points on a 
2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance 
between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if 
there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
'''

from heapq import *
def minCostConnectPoints(points):
    n = len(points)
    V = n        # noOfNodes
    adj = [[] for _ in range(V)] 
    
    def create_adj(adj, V):
        for i in range(V):
            for j in range(V):
                if i == j:
                    continue
                wt = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, wt])

    create_adj(adj, V)
    for i in adj:
        print(i)
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
            node = adjel[0]
            edgeWt = adjel[1]
            if not visited[node]:
                heappush(priorityQ,(edgeWt, node))
    return summ
        
if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    res = minCostConnectPoints(points)
    
    print("the sum of the weights of the edges in the Minimum Spanning Tree (MST): ", res)
    
