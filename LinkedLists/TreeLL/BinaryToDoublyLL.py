"""
# Binary Tree to Doubly Linked List

Given a Binary Tree (BT), convert it to a Doubly Linked List (DLL) in place. The left and right pointers in nodes 
will be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the 
same as the order of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the 
head node of the DLL.

Note: h is the tree's height, and this space is used implicitly for the recursion stack.

TreeToList

Examples:

Input:
      1
    /  \
   3    2
Output:
3 1 2 
2 1 3

Explanation: DLL would be 3<=>1<=>2

"""
from collections import deque
import sys

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

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
    
  
 
def BinaryToDoublyLL(root):
    prev, head = None, None
    def inorder(root):
        nonlocal prev, head
        if not root:
            return None
        
        inorder(root.left)
        if not prev:
            head = root
        else:
            root.left = prev
            prev.right = root
        prev = root
        inorder(root.right)
    inorder(root)
    return head



def print_doubly_linked_list(head):
    prev = None
    sys.stdout.flush()
    print('None -> ', end = "")
    while(head != None):
        print(head.data, end=" -> ")
        prev=head
        head=head.right
    print('None')
    print('None <- ', end = "")
    while(prev != None):
        print(prev.data, end=" <- ")
        prev=prev.left
    print('None')
    
    
if __name__ == "__main__":
    root = Tree(90)
    root.left = Tree(80)
    root.right = Tree(75)
    root.left.left = Tree(70)
    root.left.right =Tree(79)
    root.right.left = Tree(69)
    root.right.right = Tree(65)
    
    print("Level Order Traversal: ")
    level = levelOrder(root)
    print(level)
    print("Doubly Linked List: ")
    print_doubly_linked_list(BinaryToDoublyLL(root))
