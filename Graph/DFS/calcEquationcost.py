'''
#   Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where 
equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi
is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you 
must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in
division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer 
cannot be determined for them.


Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

'''

from typing import List  # Import List for type hinting
from collections import defaultdict  # Import defaultdict for easy graph construction

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph as an adjacency list where each node is a variable
        graph = defaultdict(dict)  # Initialize the graph dictionary
        
        for (A, B), val in zip(equations, values):  # Iterate over equations and their corresponding values
            graph[A][B] = val  # Set the edge from A to B as val (A / B = val)
            graph[B][A] =1 / val  # Set the edge from B to A as1/val (B / A = 1/val)
        
        # Helper function to perform DFS search
        def dfs(src, dst, visited):  # src: current variable, dst: target variable, visited: set of visited variables
            if src not in graph or dst not in graph:  # If either variable is not in the graph, return-1
                return -1.0            
            if src == dst:  # If both variables are the same, result is 1
                return 1.0
            visited.add(src)  # Mark current variable as visited
            for neighbor, value in graph[src].items():  # Iterate over neighbors and their edge values
                if neighbor in visited:  # Skip if already visited to prevent cycles
                    continue
                result = dfs(neighbor, dst, visited)  # Recursively search from neighbor to destination
                if result != -1.0:  # If a valid path is found
                    return value * result  # Multiply current edge value with result from neighbor onwards
            return -1.0  # If no valid path is found, return -1
        
        results = []  # List to store results for each query
        for C, D in queries:  # For each query
            results.append(dfs(C, D, set()))  # Perform DFS from C to D with a fresh visited set
        
        return results  # Return the list of results
        
if __name__ == "__main__":
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    
    obj = Solution()
    print(f"Path cost to reach from sourc to destination in queries: {obj.calcEquation(equations, values, queries)}")
    
