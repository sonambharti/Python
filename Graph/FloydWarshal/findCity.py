"""
# City With the Smallest Number of Neighbors at a Threshold Distance
There are n cities labeled from 0 to n-1 with m edges connecting them. Given the array edges 
where edges[i] = [fromi , toi ,weighti]  represents a bidirectional and weighted edge between 
cities fromi and toi, and given the integer distanceThreshold. You need to find out a city 
with the smallest number of cities that are reachable through some path and whose distance is 
at most Threshold Distance. If there are multiple such cities, our answer will be the city with 
the greatest label.

Note: The distance of a path connecting cities i and j is equal to the sum of the edge's weights 
along that path.

Example 1:

Input:
n = 4, m = 4
edges = [[0, 1, 3],
         [1, 2, 1], 
         [1, 3, 4],  
         [2, 3, 1]]
distanceThreshold = 4
Output:
3
Explaination:

The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since
it has the greatest number.
"""

import heapq
def findCity(n, m, edges, distanceThreshold):
    # code here
    
    dist_mat = [[float('infinity')]*n for _ in range(n)]
    for edge in edges:
        dist_mat[edge[0]][edge[1]] = dist_mat[edge[1]][edge[0]] = edge[2]
    
    for i in range(n):
        dist_mat[i][i] = 0
    
        
    for via in range(n):
        for u in range(n):
            for v in range(n):
                if ((dist_mat[u][via]!=float('infinity')) and (dist_mat[via][v])!=float('infinity')) and (dist_mat[u][v] > dist_mat[u][via] + dist_mat[via][v]):
                    dist_mat[u][v] = dist_mat[u][via] + dist_mat[via][v]
                if (dist_mat[u][v] > dist_mat[u][via] + dist_mat[via][v]):
                    dist_mat[u][v] = dist_mat[u][via] + dist_mat[via][v]
        
    max_city = n
    ans = -1
    for u in range(n):
        count = 0
        for v in range(n):
            if (dist_mat[u][v] <= distanceThreshold):
                count += 1
            
        if (count <= max_city):
            max_city = count
            ans = u
    print("Shortest distance of each node from each node\n")
    for row in dist_mat:
        print(row)
    return ans
    
if __name__ == "__main__":
    # n = 5 
    # m = 6
    # edges = [[0, 1, 2],
    #          [0, 4, 8],
    #          [1, 2, 3], 
    #          [1, 4, 2], 
    #          [2, 3, 1],
    #          [3, 4, 1]]
    # distanceThreshold = 2
    n = 4
    m = 4
    edges = [[0, 1, 3],
        [1, 2, 1], 
        [1, 3, 4],  
        [2, 3, 1]]
    distanceThreshold = 4
    res = findCity(n, m, edges, distanceThreshold)
    print("city with the smallest number of cities that are reachable through some path and whose distance is at most Threshold Distance is: ", res)
    
    
    
