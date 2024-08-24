"""
# Shortest path in Directed Acyclic Graph

Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector) 
edges[ ][ ] of length M, where there is a directed edge from edge[i][0] to edge[i][1] with a 
distance of edge[i][2] for all i.

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach 
any vertex, then return -1 for that vertex.

Example1:

Input:
N = 4, M = 2
edge = [[0,1,2],[0,2,1]]
Output:
0 2 1 -1
Explanation:
Shortest path from 0 to 1 is 0->1 with edge weight 2. 
Shortest path from 0 to 2 is 0->2 with edge weight 1.
There is no way we can reach 3, so it's -1 for 3.
"""

adjList = []
    
def shortestPath(edges, n, m):
    def create_dir_adj_list(edges, numOfNodes):
        global adjList
        # numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
        adjList = [[]*numOfNodes for _ in range(numOfNodes)]
        for i in range(len(edges)):
            adjList[edges[i][0]].append([edges[i][1], edges[i][2]]) # directed
    
    
    def topoSort(n, adjList, node, vis, st):
        vis[node] = True
        for el in adjList[node]:
            adjel = el[0]
            if vis[adjel]==False:
                topoSort(n, adjList, adjel, vis, st)
        st.append(node)
                    

    
    vis = [False]*n
    st = []
    create_dir_adj_list(edges, n)
    
    for i in range(n):
        if not vis[i]:
            topoSort(n, adjList, i, vis, st)
            
    
    dist = [float('inf')]*n
    dist[0] = 0
    while st:
        el = st.pop()
        for adjel in adjList[el]:
            adjeln = adjel[0]
            wt = adjel[1]
            if (dist[adjeln] > (dist[el] + wt)):
                dist[adjeln] = dist[el] + wt
                
                
    for i in range(n):
        if dist[i] == float('inf'):
            dist[i] = -1
    return dist
    

if __name__ == "__main__":
    edges =  [[0,1,2],[0,2,1]]
    numOfNodes = 4
    numOfEdges = 2
    res = shortestPath(edges, numOfNodes, numOfEdges)
    print("Shortest Path in a directed acyclic graph from source: ", res)
