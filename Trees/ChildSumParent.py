#find child sum parent tree

from collections import deque

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def childSumParent(root):
    if not root or not root.left and not root.right:
        return 1
        
    l = root.left.data
    r = root.right.data
    
    if root.data == l+r and childSumParent(root.left)==1 and childSumParent(root.right)==1:
        return 1
    
    return 0
    
    
root = Tree(90)
root.left = Tree(45)
root.right = Tree(45)
root.left.left = Tree(30)
root.left.right =Tree(15)
root.right.left = Tree(25)
root.right.right = Tree(20)


print("Given tree is child sum Parent: ", childSumParent(root))


   
root1 = Tree(90)
root1.left = Tree(45)
root1.right = Tree(55)
root1.left.left = Tree(30)
root1.left.right =Tree(15)
root1.right.left = Tree(25)
root1.right.right = Tree(20)


print("Given tree is child sum Parent: ", childSumParent(root1))

