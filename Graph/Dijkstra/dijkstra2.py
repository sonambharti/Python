"""
# Dijkstra Algorithm

Given a weighted, undirected and connected graph of V vertices and an adjacency list adj 
where adj[i] is a list of lists containing two integers where the first integer of each 
list j denotes there is edge between i and j , second integers corresponds to the weight 
of that  edge . You are given the source vertex S and You to Find the shortest distance 
of all the vertex's from the source vertex S. You have to return a list of integers 
denoting shortest distance between each node and Source vertex S.
 

Note: The Graph doesn't contain any negative weight cycle.

 

Example 1:

Input:
V = 2
adj [] = {{{1, 9}}, {{0, 9}}}
S = 0
Output:
0 9
"""

import heapq


#Function to find the shortest distance of all the vertices
#from the source vertex S.
def dijkstra(V, adj, S):
    #code here
    distance = [float('infinity') for _ in range(V)]
    distance[S] = 0
    
    queue = [(0, S)]
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
    return distance

    
if __name__ == "__main__":
    V = 3 
    E = 3
    adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
    S = 2
    res = dijkstra(V, adj, S)
    print("Minimum distance from source, s: ", res)
