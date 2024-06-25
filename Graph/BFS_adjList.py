# Implement BFS using adjacency list....
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
    
def bfs(adjList, n):
    # using BFS
    print("BFS Traversal: \n")
    vis = set()
    adj = adjList
    
    for i in range(n):
        if i in vis:
            continue
        
        vis.add(i)
        q = deque([i])
        while q:
            el = q.pop()
            print(el, end=" ")
            for adjel in (adj[i]):
                if adjel not in vis:
                    vis.add(adjel)
                    q.appendleft(adjel)
        

if __name__ == "__main__":
    edges = [[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]]
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    create_dir_adj_list(edges, numOfNodes)
    print("Directed Adjecency List....\n")
    print(adjList)
    bfs(adjList, numOfNodes)
    
