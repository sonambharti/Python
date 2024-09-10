'''
# Circle of Strings

Given an array arr of lowercase strings, determine if the strings can be chained together to 
form a circle.
A string X can be chained together with another string Y if the last character of X is the
same as the first character of Y. If every string of the array can be chained with exactly 
two strings of the array(one with the first character and the second with the last character 
of the string), it will form a circle.

For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the
given strings can be chained as "for", "rig", "geek" and "kaf"

Examples

Input: arr[] = ["abc", "bcd", "cdf"]
Output: 0
Explaination: These strings can't form a circle because no string has 'd'at the starting index.

Input: arr[] = ["ab" , "bc", "cd", "da"]
Output: 1
Explaination: These strings can form a circle of strings.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

'''

from collections import defaultdict

def canBeChained(arr):
    # Step 1: Build graph and in-degree, out-degree maps
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    # Step 2: Populate the graph and degree counts
    for word in arr:
        start = word[0]
        end = word[-1]
        graph[start].append(end)
        out_degree[start] += 1
        in_degree[end] += 1

    # Step 3: Check if in-degree matches out-degree for each node
    for char in set(in_degree.keys()).union(out_degree.keys()):
        if in_degree[char] != out_degree[char]:
            return 0

    # Step 4: DFS to check if the graph is strongly connected
    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    # Find a starting node with out-degree > 0
    start_node = arr[0][0]
    
    # Step 5: Check if all nodes are reachable using DFS
    visited = set()
    dfs(start_node, visited)
    
    # Collect all characters that have either in-degree or out-degree > 0
    all_chars_involved = set(in_degree.keys()).union(out_degree.keys())
    
    return 1 if visited == all_chars_involved else 0



# Example usage:
if __name__ == "__main__":
    arr1 = ["abc", "bcd", "cdf"]
    print(canBeChained(arr1))  # Output: 0
    
    arr2 = ["ab", "bc", "cd", "da"]
    print(canBeChained(arr2))  # Output: 1

