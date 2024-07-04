"""
# Bipartite Graph

Given an adjacency list of a graph adj of V no. of vertices having 0 based index. 
Check whether the graph is bipartite or not.

A bipartite graph is a graph in which the vertices can be divided into two disjoint sets, 
such that no two vertices within the same set are adjacent. In other words, it is a graph 
in which every edge connects a vertex of one set to a vertex of the other set.

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
    
    
def isBipartite(V, adj):
	#code here
	q = deque()
	color = [-1]*V
	
	def bfs(adj, sr, color):
	    q.appendleft(sr)
	    color[sr] = 0
	    while q:
	        el = q.pop()
	        for adjel in adj[el]:
	            if color[adjel]==-1:
	                q.appendleft(adjel)
	                if color[el]==0:
	                    color[adjel]=1
	                else:
	                    color[adjel]=0
	            else:
	                if color[el] == color[adjel]:
	                    return False
	    return True
	for i in range(V):
	    if color[i] == -1:
	        if not bfs(adj, i, color):
	            return False
	return True
	            

if __name__ == "__main__":
    edges = [[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]]
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    create_dir_adj_list(edges, numOfNodes)
    print("Is Bipartite: ", isBipartite(numOfNodes, adjList))
