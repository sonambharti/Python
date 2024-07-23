"""
# Shortest Path in Weighted undirected graph

You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges 
along with their weights. Find the shortest path between the vertex 1 and the vertex n,  if 
there exists a path, and return a list of integers whose first element is the weight of the 
path, and the rest consist of the nodes on that path. If no path exists, then return a list 
containing a single element -1.

The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, 
and w is the weight of that edge.

Note: The driver code here will first check if the weight of the path returned is equal to the 
sum of the weights along the nodes on that path, if equal it will output the weight of the path, 
else -2. In case the list contains only a single element (-1) it will simply output -1. 

Examples :

Input: n = 5, m= 6, edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
Output: 5
Explanation: Shortest path from 1 to n is by the path 1 4 3 5 whose weight is 5. 
"""

import heapq


#Function to find the shortest distance of all the vertices
#from the source vertex S.
def shortestPath(n, m, edges):
    # code here
    
    adj = [[] for _ in range(n+1)]
    for edge in edges:
        adj[edge[0]].append((edge[1], edge[2]))
        adj[edge[1]].append((edge[0], edge[2]))

    distance = [float('infinity') for _ in range(0, n+1)]
    distance[1] = 0
    dpath = [i for i in range(0, n+2)]
    path = []
    queue = [(0, 1)]
    # print(queue)
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distance[current_node]:
            continue
        
        for adje in adj[current_node]:
            adjn = adje[0]
            adjw = adje[1]
            
            distance_through_current_node = current_distance + adjw
            if distance_through_current_node < distance[adjn]:
                distance[adjn] = distance_through_current_node
                heapq.heappush(queue, (distance[adjn], adjn))
                dpath[adjn] = current_node
    
    if distance[n] == float('infinity'):
        return [-1]
    
    node = n
    while dpath[node] != node:
        path.append(node)
        node = dpath[node]
        
    path.append(1)  
    # path.append(distance[n])
    # return path[::-1]
    rev_path = path[::-1]
    return (distance[n], rev_path)

    
if __name__ == "__main__":
    edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
    n = 5
    m = 6
    res = shortestPath(n, m, edges)
    print("Minimum distance from source, 1: ", res)
    
