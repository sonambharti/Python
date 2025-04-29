"""
# Minimum cost to connect all houses in a city

Given a 2D array houses[][], consisting of n 2D coordinates {x, y} where each coordinate represents the
location of each house, the task is to find the minimum cost to connect all the houses of the city.

The cost of connecting two houses is the Manhattan Distance between the two points (xi, yi) and (xj, yj) 
i.e., |xi – xj| + |yi – yj|, where |p| denotes the absolute value of p.

Examples :

Input: n = 5 houses[][] = [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]]
Output: 105
Explanation:
Connect house 1 (0, 7) and house 2 (0, 9) with cost = 2
Connect house 1 (0, 7) and house 3 (20, 7) with cost = 20
Connect house 3 (20, 7) with house 4 (30, 7) with cost = 10 
At last, connect house 4 (30, 7) with house 5 (40, 70) with cost 73.
All the houses are connected now.
The overall minimum cost is 2 + 10 + 20 + 73 = 105.

Input: n = 4 houses[][] = [[0, 0], [1, 1], [1, 3], [3, 0]]
Output: 7
Explanation: 
Connect house 1 (0, 0) with house 2 (1, 1) with cost = 2
Connect house 2 (1, 1) with house 3 (1, 3) with cost = 2 
Connect house 1 (0, 0) with house 4 (3, 0) with cost = 3 
The overall minimum cost is 3 + 2 + 2 = 7.
"""

from heapq import *

class Solution:
    def manhattanDist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
    def minCost(self, houses):
        # code here
        V = len(houses)
        visited = [False] * V
        minDist = [float("inf")] * n
        summ = 0
        priorityQ = [(0, 0)]
        
        # create priority queue using min-heap
        heapify(priorityQ)
        
        while priorityQ:
            # min heap pop - poped element will always have minimum weight
            wt, el = heappop(priorityQ) 
            if visited[el]: # if already visited then leave
                continue
                
            # if not visited, mark it visited and add the value to sum
            visited[el] = True 
            summ += wt
    
            # check all the adjacent nodes of the poped node
            for v in range(n): 
                if not visited[v]:
                    dist = self.manhattanDist(houses[el], houses[v])
                    if dist < minDist[v]:
                        minDist[v] = dist
                        heappush(priorityQ,(dist, v)) # push the node along with the weight in priority queue
        return summ
    
if __name__ == "__main__":
    n = 5 
    houses = [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]]
    obj = Solution()
    res = obj.minCost(houses)
    print("Minimum Weight Cycle: ", res)
