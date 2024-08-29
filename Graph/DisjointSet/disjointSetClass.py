'''
# Disjoint Set 

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
