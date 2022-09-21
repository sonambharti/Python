#Print path from one given node to other given node

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if not root:
        return 0
            
    return max(height(root.left), height(root.right))+1
        
        
def isBalanced(root):
    
    if not root:
        return 1
        
    lh = height(root.left)
    rh = height(root.right)
        
    if (abs(lh-rh) <= 1) and isBalanced(root.left) == 1 and isBalanced(root.right) == 1:
        return 1
            
    return 0

    

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


print(isBalanced(root))
