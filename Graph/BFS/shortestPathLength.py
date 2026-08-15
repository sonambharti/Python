"""
# 847. Shortest Path Visiting All Nodes

You have an undirected, connected graph of n nodes labeled from 0 to n - 1. 
You are given an array graph where graph[i] is a list of all the nodes connected 
with node i by an edge.

Return the length of the shortest path that visits every node. You may start and
stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:
Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
"""
from typing import List 
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        q = deque()

        # Start BFS from every node
        for node in range(n):
            visited_nodes = frozenset([node])
            # print(visited_nodes)
            q.append((node, visited_nodes))

        visited_states = set()

        for node in range(n):
            visited_states.add(
                (node, frozenset([node]))
            )

        distance = 0

        while q:

            for _ in range(len(q)):

                node, visited_nodes = q.popleft()
                # print(f"visited_nodes: {visited_nodes}")

                # All nodes have been visited
                if len(visited_nodes) == n:
                    return distance

                for neighbor in graph[node]:

                    new_visited = visited_nodes | frozenset([neighbor])
                    # print(f"new_visited: {new_visited}")

                    state = (neighbor, new_visited)

                    if state not in visited_states:
                        visited_states.add(state)
                        q.append((neighbor, new_visited))

            distance += 1
        return distance

if __name__ == "__main__":
    graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    res = Solution().shortestPathLength(graph)
    print(res)
