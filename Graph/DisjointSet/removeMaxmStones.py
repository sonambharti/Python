'''
#  947. Most Stones Removed with Same Row or Column

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the 
largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

'''
class DisjointSet:
    def __init__(self, noOfNodes):
        self.parent = [i for i in range(noOfNodes + 1)]
        self.rank = [0 for _ in range(noOfNodes + 1)]
        self.size = [1 for _ in range(noOfNodes + 1)]
    
    
    def findUltimateParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]
        
        
    # Will make the links-between-nodes using DisjointSet UnionByRank
    def UnionByRank(self, edge):
        firstParent = self.findUltimateParent(edge[0])
        secParent = self.findUltimateParent(edge[1])
        if firstParent == secParent:
            return
        
        if self.rank[firstParent] < self.rank[secParent]:
            self.parent[firstParent] = secParent
            
        elif self.rank[firstParent] > self.rank[secParent]:
            self.parent[secParent] = firstParent
            
        else:
            self.parent[secParent] = firstParent # Taking convention of connecting 2nd parent below to 1st Parent
            self.rank[firstParent] += 1
        
    
def removeMaxmStones(stones):
    n = len(stones)
    maxRow, maxCol = 0, 0

    for cords in stones:
        maxRow = max(maxRow, cords[0])
        maxCol = max(maxCol, cords[1])

    disjoint = DisjointSet(maxRow + maxCol + 1)
    stoneNodes = {}
    # stoneNodes = set()
    for cords in stones:
        nodeRow = cords[0]
        nodeCol = cords[1] + maxRow + 1
        disjoint.UnionByRank((nodeRow, nodeCol))
        # taking update
        stoneNodes[nodeRow] = 1
        stoneNodes[nodeCol] = 1
        # stoneNodes.add(nodeRow)
        # stoneNodes.add(nodeCol)

    count = 0
    # For dictionary
    for key, value in stoneNodes.items():
        if disjoint.findUltimateParent(key) == key:
            count += 1

    # For sets
    # for stone in stoneNodes:
    #     if disjoint.findUltimateParent(stone) == stone:
    #         count += 1
    
    # No of stones removed = (Total no of stones - No. of Components) in the graph
    res = n - count
    
    return res
    

if __name__ == "__main__":
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    res = removeMaxmStones(stones)
    
    print("The sum of the weights of the edges in the Minimum Spanning Tree (MST): ", res)
   
    
