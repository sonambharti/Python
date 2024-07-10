"""
# Eventual Safe States

A directed graph of V vertices and E edges is given in the form of an adjacency list adj. 
Each node of the graph is labelled with a distinct integer in the range 0 to V - 1.

A node is a terminal node if there are no outgoing edges. A node is a safe node if every 
possible path starting from that node leads to a terminal node.

You have to return an array containing all the safe nodes of the graph. The answer should be 
sorted in ascending order.

"""


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
    

def eventualSafeNodes(V, adj):
    # code here
    def dfs_recursive_path(adj, vis, path, el, safe):
        vis[el] = True
        path[el] = True
        safe[el] = False
        for adjel in adj[el]:
            if not vis[adjel]:
                if dfs_recursive_path(adj, vis, path, adjel, safe):
                    safe[el] = False
                    return True
            elif path[adjel]:
                # print(f"cycle found at {el} - {adjel}")
                safe[el] = False
                return True
        safe[el] = True
        path[el] = False
        return False
                
        
    vis = [False]*V
    safe = [False]*V
    path = [False]*V
    for i in range(V):
        if not vis[i]:
            dfs_recursive_path(adj, vis, path, i, safe)
    
    res = []
    for i in range(V):
        if safe[i]:
            res.append(i)
    return res



if __name__ == "__main__":
    edges = [[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]]
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    create_dir_adj_list(edges, numOfNodes)
    print("Directed Adjecency List....\n")
    print(adjList)
    res = eventualSafeNodes(numOfNodes, adjList)
    print("Resultant an array containing all the safe nodes of the graph: ", res)
