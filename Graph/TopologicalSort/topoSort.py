"""
# Topological Sort
Given an adjacency list for a Directed Acyclic Graph (DAG) where adj_list[i] contains a list of 
all vertices j such that there is a directed edge from vertex i to vertex j, with  V  vertices 
and E  edges, your task is to find any valid topological sorting of the graph.

 

In a topological sort, for every directed edge u -> v,  u must come before v in the ordering.

Topological sort -> only applicable on directed acyclic graph

"""

adjList = []
def create_dir_adj_list(edges, numOfNodes):
    global adjList
    # numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    adjList = [[]*numOfNodes for _ in range(numOfNodes)]
    for i in range(len(edges)):
        adjList[edges[i][0]].append(edges[i][1]) # directed
        # adjList[edges[i][1]].append(edges[i][0]) # undirected
        
def topoSort(numOfNodes, adj):
    # Code here
    st = []
    V = numOfNodes
    vis = [False]*V
    def dfs_recursion(adj, node, vis):
        vis[node] = True
        for i in adj[node]:
            if vis[i]==False:
                dfs_recursion(adj, i, vis)
        st.append(node)
                
    for i in range(V):
        if not vis[i]:
            dfs_recursion(adj, i, vis)
            
    res = []
    for i in range(V):
        res.append(st.pop())
    
    return res

if __name__ == "__main__":
    
    edges = [[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]]
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    create_dir_adj_list(edges, numOfNodes)
    res = topoSort(numOfNodes, adjList)
    print("Topological Sorted elements: ", res)
