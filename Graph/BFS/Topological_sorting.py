"""
# Topological sorting

Given an adjacency list for a Directed Acyclic Graph (DAG) where adj_list[i] contains a list of 
all vertices j such that there is a directed edge from vertex i to vertex j, with  V  vertices 
and E  edges, your task is to find any valid topological sorting of the graph.

 

In a topological sort, for every directed edge u -> v,  u must come before v in the ordering.

 
"""

from collections import deque
adjList = []
def create_dir_adj_list(edges, numOfNodes):
    global adjList
    # numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    adjList = [[]*numOfNodes for _ in range(numOfNodes)]
    for i in range(len(edges)):
        adjList[edges[i][0]].append(edges[i][1]) # directed
        # adjList[edges[i][1]].append(edges[i][0]) # undirected
    # print(adjList)
    # return adjList
    
def topoSort(V, adj):
    # Code here
    in_degree = {i: 0 for i in range(V)}
    res = []
    for i in range(V):
        for node in adj[i]:
            in_degree[node] += 1
    
    q = deque()
    for i in in_degree:
        if in_degree[i] == 0:
            q.appendleft(i)
            
    while q:
        el = q.pop()
        print(type(el))
        res.append(el)
        for adjel in adj[el]:
            in_degree[adjel] -= 1
            if in_degree[adjel] == 0:
                q.appendleft(adjel)
    return res

if __name__ == "__main__":
    edges = [[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]]
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    create_dir_adj_list(edges, numOfNodes)
    print("Topological Sort: ", topoSort(numOfNodes, adjList))
