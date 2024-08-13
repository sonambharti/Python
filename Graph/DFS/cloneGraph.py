'''

# 133. Clone Graph 

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, 
the first node with val == 1, the second node with val == 2, and so on. The graph is 
represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each 
list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the 
given node as a reference to the cloned graph.

 

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of 
only one node with val = 1 and it does not have any neighbors.


'''
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional, List

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to keep track of copied nodes
        oldToNew = {}

        # DFS function to clone the graph
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            # Create a copy of the current node
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # Iterate through the neighbors to recursively copy them
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)
        
# Helper function to build a graph from an adjacency list
def build_graph(adjList: List[List[int]]) -> Node:
    if not adjList:
        return None
    
    nodes = {i: Node(i) for i in range(1, len(adjList) + 1)}
    
    for i, neighbors in enumerate(adjList):
        node = nodes[i + 1]
        for neighbor in neighbors:
            node.neighbors.append(nodes[neighbor])
    
    return nodes[1]

# Helper function to convert a graph to an adjacency list for comparison
def graph_to_adjlist(node: Node) -> List[List[int]]:
    adjList = []
    visited = {}
    
    def dfs(node):
        if node.val in visited:
            return
        visited[node.val] = node
        while len(adjList) < node.val:
            adjList.append([])
        adjList[node.val - 1] = [neighbor.val for neighbor in node.neighbors]
        for neighbor in node.neighbors:
            dfs(neighbor)
    
    dfs(node)
    return adjList

    
if __name__ == "__main__":
    # Example usage:
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    graph = build_graph(adjList)
    sol = Solution()
    cloned_graph = sol.cloneGraph(graph)
    cloned_adjList = graph_to_adjlist(cloned_graph)
    
    print(cloned_adjList)  # Output: [[2,4],[1,3],[2,4],[1,3]]
