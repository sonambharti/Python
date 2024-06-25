"""
Number of Good Components -> DFS Graph
Given an undirected graph with v vertices(numbered from 1 to v) and e edges. 
Find the number of good components in the graph.
A component of the graph is good if and only if the component is fully connected.
Note: A fully connected component is a subgraph of a given graph such that there's an edge 
between every pair of vertices in the component, the given graph can be a disconnected graph. 

Example 1:
e=3 
v=3
edges={{1, 2},{1, 3},{3, 2}}
Output: 
1
Explanation: 
We can see that there is only one component in the graph and in this component there is a edge 
between any two vertces.

Example 2:
e=5 
v=7
edges={{1, 2},{7, 2},{3, 5},{3, 4},{4, 5}}
Output: 
2
Explanation: 
We can see that there are 3 components in the graph. For 1-2-7 there is no edge between 1 to 7, 
so it is not a fully connected component. Rest 2 are individually fully connected component.
"""

from typing import List
from collections import defaultdict

class Solution:
    # Function to find the number of good components in a given undirected graph
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        for fro, to in edges:
            graph[fro].append(to)
            graph[to].append(fro)

        # Define a helper function for Depth-First Search (DFS)
        def dfs(vertex, nei):
            # Mark the current vertex as visited
            vis.add(vertex)
            # Increment the count of vertices in the current component
            count += 1
            # Check if the current component is fully connected
            if len(graph[vertex])!= nei:
                flag = False
            # Recursively visit the adjacent vertices
            for n in graph[vertex]:
                if n not in vis:
                    dfs(n, nei)
            # Update the flag based on the connectivity of the current component
            flag = flag & True

        # Initialize the answer as 0
        ans = 0
        # Initialize a set to keep track of visited vertices
        vis = set()
        # Iterate through all the vertices
        for i in range(1, v+1):
            # Initialize the count of vertices in the current component
            count = -1
            # Initialize the flag to check if the current component is fully connected
            flag = True
            # If the vertex is not visited, perform DFS
            if i not in vis:
                dfs(i, len(graph[i]))
                # If the current component is fully connected, increment the answer
                if flag and count == len(graph[i]):
                    ans += 1
        # Return the answer
        return ans



class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        e = int(input())

        v = int(input())

        edges = IntMatrix().Input(e, 2)

        obj = Solution()
        res = obj.findNumberOfGoodComponent(e, v, edges)

        print(res)
