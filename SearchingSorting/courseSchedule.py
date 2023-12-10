'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have 
finished course 1. So it is impossible.


'''


# This problem is solved using Topological sort...

def canFinish(numCourses, prerequisites):
    graph = {x: [0, set()] for x in range(numCourses)}
    for s,d in prerequisites:
        graph[s][1].add(d)
        graph[d][0] += 1
    
    q = [x for x in graph.keys() if graph[x][0]==0]

    while len(q):
        nodeid = q.pop(0)
        node = graph[nodeid]
        del graph[nodeid]

        for adjnodeid in node[1]:
            graph[adjnodeid][0] -= 1
            if graph[adjnodeid][0] == 0:
                q.append(adjnodeid)
    return not len(graph)
    

if __name__ == "__main__":
  numCourses1 = 2
  prerequisites1 = [[1,0]]  
  res1 = canFinish(numCourses1, prerequisites1)
  print("you can finish all courses or not: ", res1)
  
  numCourses2 = 2
  prerequisites2 = [[1,0],[0,1]]
  res2 = canFinish(numCourses2, prerequisites2)
  print("you can finish all courses or not: ", res2)
