'''
# Burning Tree
Given a binary tree and a node data called target. Find the minimum time required to 
burn the complete binary tree if the target is set on fire. It is known that in 1 second 
all nodes connected to a given node get burned. That is its left child, right child, and parent.
Note: The tree contains unique values.


Examples : 

Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      6
       / \      \
      7   8      9
                   \
                   10
Target Node = 8
Output: 7

'''
from collections import deque, defaultdict

# Tree class to create a tree 
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
class Solution:
    def minTime(self, root, target):
        # Helper function to map each node to its parent
        def mapParent(root, mapp, target):
            Q = deque([root])
            target_node = None
            while Q:
                node = Q.popleft()  # pop from left (front)
                
                if node.data == target:
                    target_node = node
                
                if node.left:
                    mapp[node.left] = node
                    Q.append(node.left)
                    
                if node.right:
                    mapp[node.right] = node
                    Q.append(node.right)
                    
            return target_node

        # BFS to find the maximum time required to burn the entire tree
        def findTimeUsingBFS(mapp, start):
            q = deque([start])
            vis = defaultdict(lambda: False)  # Initialize all nodes as not visited
            vis[start] = True
            maxi = 0
            
            while q:
                sz = len(q)
                fl = False
                
                for _ in range(sz):
                    node = q.popleft()  # pop from left (front)
                    
                    # Check left child
                    if node.left and not vis[node.left]:
                        fl = True
                        vis[node.left] = True
                        q.append(node.left)
                        
                    # Check right child
                    if node.right and not vis[node.right]:
                        fl = True
                        vis[node.right] = True
                        q.append(node.right)
                        
                    # Check parent node
                    if node in mapp and not vis[mapp[node]]:
                        fl = True
                        vis[mapp[node]] = True
                        q.append(mapp[node])
                
                if fl:
                    maxi += 1  # Increase time if any node burns
            
            return maxi
        
        # Dictionary to map each node to its parent
        mapp = {}
        
        # Map all nodes to their parents and find the target node
        start = mapParent(root, mapp, target)
        
        # Find the maximum time needed to burn the entire tree
        maxTime = findTimeUsingBFS(mapp, start)
        return maxTime
        

if __name__ == "__main__":
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right =Tree(5)
    root.right.right = Tree(6)
    
    root.left.right.left =Tree(7)
    root.left.right.right =Tree(8)
    
    root.right.right.right = Tree(9)
    
    root.right.right.right.right = Tree(10)
    
    target = 8 
    
    solution = Solution()
    min_time = solution.minTime(root, target)
    
    print("Minimum Time to Burn the whole Binary Tree: ", min_time)
    
    
    
