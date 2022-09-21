#Check if a given Binary Tree is Symmetric or not.

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sameTree(root1, root2):
    if not root1 and not root2:
        return True
        
    if root1 and root2:
        if(root1.data == root2.data):
            return sameTree(root1.left, root2.right) and sameTree(root2.left, root1.right)
            
    return False
  

def isSymmetric(root):
    # Your Code Here
    if not root:
        return True
          
    lh = root.left
    rh = root.right
        
        
    return sameTree(lh, rh)

    



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


print(isSymmetric(root))


root1 = Tree(1)
root1.left = Tree(2)
root1.right = Tree(2)
root1.left.left = Tree(3)
root1.left.right =Tree(3)
root1.right.left = Tree(3)
root1.right.right = Tree(3)


print(isSymmetric(root1))
