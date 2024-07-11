"""
# Eventual Safe States

A directed graph of V vertices and E edges is given in the form of an adjacency list adj. 
Each node of the graph is labelled with a distinct integer in the range 0 to V - 1.

A node is a terminal node if there are no outgoing edges. A node is a safe node if every 
possible path starting from that node leads to a terminal node.

You have to return an array containing all the safe nodes of the graph. The answer should be 
sorted in ascending order.

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
    

in_degree = {}   
def eventualSafeNodes(V, adj):
    # code here
    global in_degree
    adjList = []
    def create_dir_adj_list(adj, numOfNodes):
        global in_degree
        in_degree = {i: 0 for i in range(V)}
        # numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
        adjList = [[]*numOfNodes for _ in range(numOfNodes)]
        for i in range(V):
            for el in adj[i]: 
                in_degree[i] += 1
                adjList[el].append(i) # directed
        return adjList
    
    adjList = create_dir_adj_list(adj, V) 
    # in_degree = {i: 0 for i in range(V)}
    # for i in range(V):
    #     for node in adjList[i]:
    #         in_degree[node] += 1
    
    q = deque()
    for i in in_degree:
        if in_degree[i] == 0:
            q.appendleft(i)
            
    res = []
    while q:
        el = q.pop()
        res.append(el)
        for adjel in adjList[el]:
            in_degree[adjel] -= 1
            if in_degree[adjel] == 0:
                q.appendleft(adjel)
    res.sort()
    return res
    

if __name__ == "__main__":
    edges = [[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]]
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    create_dir_adj_list(edges, numOfNodes)
    print("Directed Adjecency List....\n")
    print(adjList)
    res = eventualSafeNodes(numOfNodes, adjList)
    print("Resultant an array containing all the safe nodes of the graph: ", res)
