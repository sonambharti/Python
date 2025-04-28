'''
#   Maximum sum of Non-adjacent nodes

Given a binary tree with a value associated with each node. Your task is to select a
subset of nodes such that the sum of their values is maximized, with the condition 
that no two selected nodes are directly connected that is, if a node is included in 
the subset, neither its parent nor its children can be included.

Examples:

Input: root[] = [11, 1, 2]

Output: 11
Explanation: The maximum sum is obtained by selecting the node 11.

Input: root[] = [1, 2, 3, 4, N, 5, 6]

Output: 16
Explanation: The maximum sum is obtained by selecting the nodes 1, 4, 5, and 6, which 
are not directly connected to each other. Their total sum is 16.
'''


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque
def levelOrder(root):
    level = []
    lst = []
    
    if not root:
        return root
        
    Q = deque([None, root])
    
    while (True):
        x = Q.pop()
        if x:
            level.append(x.data)
            if x.left:
                Q.appendleft(x.left)
            if x.right:
                Q.appendleft(x.right)
        
        else:
            lst.append(level)
            level = []
            
            if Q:
                Q.appendleft(None)
            else:
                break
            
    return lst

class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    def dfs(self, root):
        if not root:
            return [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        include = root.data + left[1] + right[1]
        exclude = max(left) + max(right)
        
        return [include, exclude]
        
    def getMaxSum(self, root):
        #code here
        res = self.dfs(root)
        return max(res)

    
if __name__ == "__main__":
    #create tree
    
    root = Tree(90)
    root.left = Tree(80)
    root.right = Tree(75)
    root.left.left = Tree(70)
    root.left.right =Tree(79)
    root.right.left = Tree(69)
    root.right.right = Tree(65)
    
    root.left.left.left = Tree(42)
    root.left.left.right = Tree(40)
    root.left.right.left = Tree(41)
    root.left.right.right = Tree(46)
    
    root.right.left.left = Tree(32)
    root.right.left.right = Tree(30)
    root.right.right.left = Tree(31)
    root.right.right.right = Tree(36)
    
    print("Level order traversal of the tree: ", levelOrder(root))
    obj = Solution()
    res = obj.getMaxSum(root)
    print("Maximum sum of Non-adjacent nodes: ", res)
