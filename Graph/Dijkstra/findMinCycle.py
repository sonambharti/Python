"""
# Minimum Weight Cycle

Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by a 
2d array edges[][], where edges[i] = [u, v, w] represents the edge between the nodes u and v having w edge weight.
Your task is to find the minimum weight cycle in this graph.

Examples:

Input: V = 5, edges[][] = [[0, 1, 2], [1, 2, 2], [1, 3, 1], [1, 4, 1], [0, 4, 3], [2, 3, 4]]

Output: 6
Explanation: 
Minimum-weighted cycle is  0 → 1 → 4 → 0 with a total weight of 6(2 + 1 + 3)

Input: V = 5, edges[][] = [[0, 1, 3], [1, 2, 2], [0, 4, 1], [1, 4, 2], [1, 3, 1], [3, 4, 2], [2, 3, 3]]

Output: 5
Explanation: 
Minimum-weighted cycle is  1 → 3 → 4 → 1 with a total weight of 5(1 + 2 + 2)

"""
from collections import defaultdict
from heapq import heappush, heappop

#from the source vertex S.
def dijkstra(V, adj, S, D):
    #code here
    INF = float('infinity')
    distance = [float('infinity') for _ in range(V)]
    distance[S] = 0
    
    queue = [(0, S)]
    # print(queue)
    
    while queue:
        current_distance, current_node = heappop(queue)
        if current_node == D:
            return current_distance
        
        for adje in adj[current_node]:
            adjn = adje[0]
            adjw = adje[1]
            
            if sorted([current_node, adjn]) == sorted((S,D)):
                continue
            
            distance_through_current_node = current_distance + adjw
            if distance_through_current_node < distance[adjn]:
                distance[adjn] = distance_through_current_node
                heappush(queue, (distance[adjn], adjn))
    return INF
    
    
#from the source vertex S.
def findMinCycle(V, edges):
    # code here
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append([v, w])
        adj[v].append([u, w])
    
    ans = float('infinity')
    for u, v, w in edges:
        ans = min(ans, dijkstra(V, adj, u, v)+w)
    return ans
    
    
if __name__ == "__main__":
    V = 5 
    edges = [[0, 1, 2], [1, 2, 2], [1, 3, 1], [1, 4, 1], [0, 4, 3], [2, 3, 4]]
    res = findMinCycle(V, edges)
    print("Minimum Weight Cycle: ", res)
