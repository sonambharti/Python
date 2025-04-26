"""
# Is Binary Tree Heap

You are given a binary tree, and the task is to determine whether it satisfies the 
properties of a max-heap.

A binary tree is considered a max-heap if it satisfies the following conditions:

Completeness: Every level of the tree, except possibly the last, is completely filled,
and all nodes are as far left as possible.
Max-Heap Property: The value of each node is greater than or equal to the values of its children.
Examples:

Input: root[] = [97, 46, 37, 12, 3, 7, 31, 6, 9]
 
Output: true
Explanation: The tree is complete and satisfies the max-heap property.
Input: root[] = [97, 46, 37, 12, 3, 7, 31, N, 2, 4] 
 
Output: false
Explanation: The tree is not complete and does not follow the Max-Heap Property, hence it is not a max-heap.



                   25		
                 /   \      
                5    21		
               / \   / \    
              4   3 9  12	                    
             / \               
            1	2          	 


"""


class Node():
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
    def isCompleteTree(self, root):
        # use bfs or level or traversal to check if any node have no left child but is having right child
        q = deque([root])
        seen_null = False
        while q:
            node = q.popleft()
            if not node:
                seen_null = True
            else:
                if seen_null:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
        
        
        
if __name__ == "__main__":
    root = Node(25)
    root.left = Node(5)
    root.right = Node(21)
    root.left.left = Node(4)
    root.left.right = Node(3)
    root.right.left = Node(9)
    root.right.right = Node(12)
    # root.left.left.left = Node(1)
    root.left.left.right = Node(2)
    
    res = levelOrder(root)
    
    print("Level Order traversal : ", res)
    
    obj = Solution()
    print("Is this tree a complete tree or not: ", obj.isCompleteTree(root))
