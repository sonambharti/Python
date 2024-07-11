"""
# Shortest Path in an undirected graph

You are given an Undirected Graph having unit weight of the edges, find the shortest 
path from src to all the vertex and if it is unreachable to reach any vertex, then 
return -1 for that vertex.

Example1:

Input:
n = 9, m= 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0
Output:
0 1 2 1 2 3 3 4 4

"""

from collections import deque
adjList = []
    
def shortestPath(edges, n, m, src):
    global adjList
    def create_dir_adj_list(edges, numOfNodes):
        global adjList
        # numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
        adjList = [[]*numOfNodes for _ in range(numOfNodes)]
        for i in range(len(edges)):
            adjList[edges[i][0]].append(edges[i][1]) 
            adjList[edges[i][1]].append(edges[i][0]) 
                
    
    # using BFS
    create_dir_adj_list(edges, n)
    dist = [float('inf')]*n
    q = deque([src])
    dist[src] = 0
    while q:
        el = q.pop()
        for adjel in adjList[el]:
            if (dist[adjel] > (dist[el] + 1)):
                dist[adjel] = dist[el] + 1
                q.appendleft(adjel)
                
    for i in range(n):
        if dist[i] == float('inf'):
            dist[i] = -1
    return dist
    

if __name__ == "__main__":
    edges = [[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    numOfEdges = len(edges)
    res = shortestPath(edges, numOfNodes, numOfEdges, 0)
    print("Shortest Path in an undirected graph from source: ", res)
