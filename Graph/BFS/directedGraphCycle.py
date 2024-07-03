"""
# Directed graph cycle
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, 
check whether it contains any cycle or not.
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
        
def isCyclic(V, adj):
    # Code here
    in_degree = {i: 0 for i in range(V)}
    count = 0
    for i in range(V):
        for node in adj[i]:
            in_degree[node] += 1
    
    q = deque()
    for i in in_degree:
        if in_degree[i] == 0:
            q.appendleft(i)
            
    while q:
        el = q.pop()
        count += 1
        for adjel in adj[el]:
            in_degree[adjel] -= 1
            if in_degree[adjel] == 0:
                q.appendleft(adjel)
    if count != V:
        return True
    return False
    
    
if __name__ == "__main__":
    
    edges = [[0,1], [1,2], [1,3], [1,4], [3,1], [3,4], [5,7], [7,6]]
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    create_dir_adj_list(edges, numOfNodes)
    res = isCyclic(numOfNodes, adjList)
    print("Cyclic graph or not:", res)
