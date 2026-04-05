"""
Given the root of a binary search tree and a number key, 
find the greatest number in the binary search tree that is less than or equal to key. 
                   5		
                 /   \      
                2    12		
               / \   / \    
              1   3 9  21	                    
                      / \               
                     19	25	 

Input: key =  24
Output: 21
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def findMaxForKey(root, key):
    greatest_so_far = -1
    if root:
        while root:
            if root.data <= key:
                greatest_so_far = root.data
                root = root.right
            else:
                root = root.left
            
    return greatest_so_far
    
root = Node(5)
root.left = Node(2)
root.right = Node(12)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(21)
root.right.right.left = Node(19)
root.right.right.right = Node(25)
key = 24
res1 = findMaxForKey(root, key)
print("greatest number in the Binary Search Tree for given key: ", res1)
