'''
# Bipartite Graph

Given a Graph with V vertices (Numbered from 0 to V-1) and E edges. Check whether the graph is bipartite or not.

A bipartite graph can be colored with two colors such that no two adjacent vertices share the same color. This
means we can divide the graph’s vertices into two distinct sets where:

All edges connect vertices from one set to vertices in the other set.
No edges exist between vertices within the same set.

Examples:

Input: V = 3, edges[][] = [[0, 1], [1,2]]
Output: true
Explanation: The given graph can be colored in two colors so, it is a bipartite graph.

Input: V = 4, edges[][] = [[0, 3], [1, 2], [3, 2], [0, 2]]
Output: false 
Explanation: The given graph cannot be colored in two colors such that color of adjacent vertices differs.
'''


class Solution:
    def create_adj_list(self, V, edges):
        adj = [[]*V for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj
            
        
    def isBipartite(self, V, edges):
        # code here
        def dfs(adj, sr, color, col):
            color[sr] = col
            for adjel in adj[sr]:
                if color[adjel] == -1:
                    if not dfs(adj, adjel, color, not col):
                        return False
                else:
                    if color[adjel] == color[sr]:
                        return False
            return True
                        
                        
        
        adj = self.create_adj_list(V, edges)
        color = [-1]*V
        
        for i in range(V):
            if color[i] == -1:
                if not dfs(adj, i, color, 0):
                    return False
        return True
        
        
if __name__ == "__main__":
    V = 3
    edges = [[0, 1], [1,2]]
    
    res = Solution().isBipartite(V, edges)
    print(f"Is this given graph Bipartite or not: {res}")
    
