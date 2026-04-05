#find diameter of a tree

from collections import deque

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

dia = 0

def helper(root):
    global dia
    if not root:
        return 0
        
    lp = helper(root.left)
    rp = helper(root.right)
    dia = max(dia, lp+rp)
    return 1+max(lp, rp)
    
    
    
def diameter(root):
    global dia
    helper(root)
    #dia+=1
    return dia
 

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

print("Diameter of the given tree is: ", diameter(root))

