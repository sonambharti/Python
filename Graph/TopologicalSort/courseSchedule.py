"""
# Course Schedule

There are a total of n tasks you have to pick, labelled from 0 to n-1. Some tasks may have 
prerequisite tasks, for example to pick task 0 you have to first finish tasks 1, which is 
expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m. Find a 
ordering of tasks you should pick to finish all tasks.
Note: There may be multiple correct orders, you just need to return any one of them. 
If it is impossible to finish all tasks, return an empty array. Driver code will print 
"No Ordering Possible", on returning an empty array. Returning any correct order will 
give the output as 1, whereas any invalid order will give the output 0. 

Example 1:

Input:
n = 2, m = 1
prerequisites = {{1, 0}}
Output:
1
Explanation:
The output 1 denotes that the order is valid. So, if you have, implemented your function 
correctly, then output would be 1 for all test cases. One possible order is [0, 1].
Example 2:

Input:
n = 4, m = 4
prerequisites = {{1, 0},
               {2, 0},
               {3, 1},
               {3, 2}}
Output:
1
Explanation:
There are a total of 4 tasks to pick. To pick task 3 you should have finished both tasks 1 and 2.
Both tasks 1 and 2 should be pick after you finished task 0. So one correct task order is [0, 1, 2, 3]. 
Another correct ordering is [0, 2, 1, 3]. Returning any of these order will result in an output of 1.
"""

#User function Template for python3
from collections import deque

adjList = []
def findOrder(n, m, prerequisites):
    # Code here
    
    def create_dir_adj_list(prerequisites, n):
        global adjList
        adjList = [[]*n for _ in range(n)]
        for i in range(len(prerequisites)):
            adjList[prerequisites[i][1]].append(prerequisites[i][0]) 
            
    def topoSort(adjList, n):
        in_degree = {i: 0 for i in range(n)}
        count = 0
        res = []
        for i in range(n):
            for node in adjList[i]:
                in_degree[node] += 1
                
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.appendleft(i)
                
        while q:
            el = q.pop()
            count += 1
            res.append(el)
            for adjel in adjList[el]:
                in_degree[adjel] -= 1
                if in_degree[adjel] == 0:
                    q.appendleft(adjel)
        if count != n:
            return []
        return res
        
    
    create_dir_adj_list(prerequisites, n)
    
    return topoSort(adjList, n)

def check(graph, N, res):
    # print("Graph: \n", graph)
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    # print("map: \n", map)
    for i in range(N):
        for v in graph[i]:
        	if map[i] > map[v]:
        		return False
    return True

if __name__=='__main__':
    n = 4
    m = 4
    prerequisites = [[1, 0],
               [2, 0],
               [3, 1],
               [3, 2]]
               
    res = findOrder(n, m, prerequisites)
    print("Order of the course: ", res)
    
    if(not len(res)):
        print("No Ordering Possible")
    else:
        if check(adjList, n, res):
            print(1)
        else:
            print(0)
    
   
