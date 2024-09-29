'''
# Disjoint Set 

A disjoint-set data structure is defined as one that keeps track of a set of elements partitioned into 
a number of disjoint (non-overlapping) subsets.

A union-find algorithm is an algorithm that performs two useful operations on such a data structure:
    1. Find: Determine which subset a particular element is in. This can determine if two elements are in the same subset.
    2. Union: Join two subsets into a single subset. Here first we have to check if the two subsets belong to the same set. 
              If not, then we cannot perform union. 

Here, We have 2 methods to find Union in Disjoint sets:
    1. Union By Rank
    2. Union By Size

** Ultimate Parent is the root node in a tree. In graph, the root parent of each node and their pareints are said to be `ultimate parent`.
** Rank - Rank of the node in a graph is the height of that node to leaf node in a 0-indexed graph.

'''

# Time Complexity = O(E.logE)


class DisjointSet:
    def __init__(self, noOfNodes):
        self.parent = [i for i in range(noOfNodes + 1)] # Initially parent of each node is the node itself.
        self.rank = [0 for _ in range(noOfNodes + 1)] # Rank of each node is initalized by 0.
        self.size = [1 for _ in range(noOfNodes + 1)] # Size of each individual node is atleast 1.
    

    # find the root parent of each node and their pareints are said to be `ultimate parent`.
    def findUltimateParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]
        
        
    # Will make the links-between-nodes using DisjointSet UnionByRank
    def UnionByRank(self, edge):
        firstParent = self.findUltimateParent(edge[0])
        secParent = self.findUltimateParent(edge[1])
        if firstParent == secParent:
            return
            
        # Here, we are doing path compression of each node. i.e. linking node to it's ultimate parent instead of it's parent.
        if self.rank[firstParent] < self.rank[secParent]: # if rank of firstParent is lesser then secParent is the Parent of firstParent
            self.parent[firstParent] = secParent
            
        elif self.rank[firstParent] > self.rank[secParent]: # if rank of secParent is lesser then firstParent is the Parent of secParent
            self.parent[secParent] = firstParent
            
        else:
            self.parent[secParent] = firstParent # Taking convention of connecting 2nd parent below to 1st Parent if rank is equal
            self.rank[firstParent] += 1          # Increasing rank of firstParent each time when we add node to next level
        
    
    
    # Will make the links-between-nodes using DisjointSet UnionBySize
    def UnionBySize(self, edge):
        firstParent = self.findUltimateParent(edge[0])
        secParent = self.findUltimateParent(edge[1])
        if firstParent == secParent:
            return
        
        if self.size[firstParent] < self.size[secParent]:
            self.parent[firstParent] = secParent
            self.size[secParent] += self.size[firstParent]
            
        else:
            self.parent[secParent] = firstParent 
            self.size[firstParent] += self.size[secParent]
        
        
if __name__ == "__main__":
    edges = [[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]]
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
        
    disjoint = DisjointSet(numOfNodes)
    # for edge in edges:
    #     disjoint.UnionByRank(edge)
    
    # print("If 3, 2 are in same components: ", disjoint.findUltimateParent(3) == disjoint.findUltimateParent(2))
    
    for edge in edges:
        disjoint.UnionBySize(edge)
    
    print("If 3, 7 are in same components: ", disjoint.findUltimateParent(3) == disjoint.findUltimateParent(7))
