"""
There are n cities. Some of them are connected, while some are not. If city a is 
connected directly with city b, and city b is connected directly with city c, then
city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities 
outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city
and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

"""
from collections import deque

def findCircleNum(isConnected):
    # using BFS
    vis = set()
    adj = isConnected
    n = len(adj)
    count = 0

    for i in range(n):
        if i in vis:
            continue
        count += 1
        vis.add(i)
        q = deque([i])
        while q:
            el = q.pop()
            for adjel in range(n):
                if adj[el][adjel]==1 and adjel not in vis:
                    vis.add(adjel)
                    q.appendleft(adjel)
    return count
    
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
res = findCircleNum(isConnected)

print("No. of Provinces = ", res)
