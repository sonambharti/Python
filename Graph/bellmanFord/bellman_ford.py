"""
# Distance from the Source (Bellman-Ford Algorithm)

Given a weighted and directed graph of V vertices and E edges, Find the shortest distance of all 
the vertex's from the source vertex S. If a vertices can't be reach from the S then mark the 
distance as 10^8. Note: If the Graph contains a negative cycle then return an array consisting of only -1.

Example 1:

Input:
E = [[0,1,9]]
S = 0
Output:
0 9
Explanation:
Shortest distance of all nodes from
source is printed.
"""

def bellman_ford(V, edges, S):
    #code here
    dist = [10**8 for _ in range(V)]
    dist[S] = 0
    
    for i in range(V):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            
            if ((dist[u] != 10**8) and (dist[u] + wt < dist[v])):
                dist[v] = dist[u] + wt
    
    # check for negative cycles         
    for edge in edges:
        u = edge[0]
        v = edge[1]
        wt = edge[2]
        
        if ((dist[u] != 10**8) and (dist[u] + wt < dist[v])):
            return [-1]
    return dist
    
if __name__ == "__main__":
    V = 3
    edges = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
    S = 2
    res = bellman_ford(V, edges, S)
    print(f"The distance of each node from the source, {S} are: {res}")
    
