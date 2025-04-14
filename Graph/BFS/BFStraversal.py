"""
# BFS of Graph

Given a connected undirected graph containing V vertices, represented by a 2-d adjacency list adj[][], where 
each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Search (BFS) 
traversal starting from vertex 0, visiting vertices from left to right according to the given adjacency list,
and return a list containing the BFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list.

Examples:

Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output: [0, 2, 3, 1, 4]
Explanation: Starting from 0, the BFS traversal will follow these steps: 
Visit 0 → Output: 0 
Visit 2 (first neighbor of 0) → Output: 0, 2 
Visit 3 (next neighbor of 0) → Output: 0, 2, 3 
Visit 1 (next neighbor of 0) → Output: 0, 2, 3, 
Visit 4 (neighbor of 2) → Final Output: 0, 2, 3, 1, 4
"""

from collections import deque
def bfs(adj):
  # code here
  n = len(adj)
  vis = [False]*n
  res = []
  vis[0] = True
  q = deque([0])
  while q:
      el = q.pop()
      res.append(el)
      for adjel in (adj[el]):
          if not vis[adjel] :
              vis[adjel] = True
              q.appendleft(adjel)
  
  return res
if __name__ == "__main__":
  adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
  res = bfs(adj)
  print("BFS traversal of the graph: ", res)
  
