'''
# 1514. Path with Maximum Probability

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list
where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability
of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from 
start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from 
the correct answer by at most 1e-5.


Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and 
the other has 0.5 * 0.5 = 0.25.

Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

'''


import heapq

def maxProbability(n, edges, succProb, start_node, end_node):
    def dijkstra(graph, start_node, end_node):
        prob = [0 for _ in range(n)]
        prob[start_node] = 1
        
        queue = [(-1.0, start_node)]
        heapq.heapify(queue)
        # print(queue)
        
        while queue:
            curr = heapq.heappop(queue)
            current_prob, current_node = -curr[0], curr[1]
            if current_node == end_node:
                return current_prob
    
            for neighbor, probability in graph[current_node]:
                distance_through_current_node = current_prob * probability
                if prob[neighbor] < distance_through_current_node:
                    prob[neighbor] = distance_through_current_node
                    heapq.heappush(queue, (-prob[neighbor], neighbor))
                
        return 0
    
    def adjListGraph(succProb, edges, n):
        adjList = [[]*n for _ in range(n)]
        for i in range(len(edges)):
            adjList[edges[i][0]].append([edges[i][1], succProb[i]]) # directed
            adjList[edges[i][1]].append([edges[i][0], succProb[i]]) # undirected
        return adjList
    

    graph = adjListGraph(succProb, edges, n)
    return dijkstra(graph, start_node, end_node)
    
            
if __name__ == "__main__":
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start_node = 0
    end_node = 2
    res = maxProbability(n, edges, succProb, start_node, end_node)
    print("The maximum probability of success to go from start to end is: ", res)
    
    
    
