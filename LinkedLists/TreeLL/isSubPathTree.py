"""
# 1367. Linked List in Binary Tree

Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to 
some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true


"""
# Tree Node Creation Class
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# Print Tree Nodes in Level Order Traversals
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
    

# Linked List Node Creation Class
class ListNode:
    def __init__(self, val=0):
        self.data = val
        self.next = None
        
        
# Print Linked List
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    

def isSubPath(root, head):
    
    def helper(list_node, tree_node):
        if not list_node:
            return True
        if not tree_node or tree_node.data != list_node.data:
            return False

        return (
            helper(list_node.next, tree_node.left) or 
            helper(list_node.next, tree_node.right)
            )

    if helper(head, root):
        return True
    if not root:
        return False
    return (
        isSubPath(root.left, head) or 
        isSubPath(root.right, head)
    )




if __name__ == "__main__":
    # Helper function to print the linked list

    # Creating a linked list with a loop
    head = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(8)
    
    head.next = node2
    node2.next = node3
    node3.next = None
    
    print("Linked list:")
    print_linked_list(head)
    
    
    root = Node(5)
    root.left = Node(2)
    root.right = Node(12)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.left.left = Node(2)
    root.right.left.left.right = Node(8)
    root.right.right = Node(21)
    root.right.right.left = Node(19)
    root.right.right.right = Node(25)
    
    print("Level Order Traversal of the tree: ", levelOrder(root))


    res = isSubPath(root, head)
    
    print("Is Linked List is sub path of the Binary tree or not:", res)
  
    
  
