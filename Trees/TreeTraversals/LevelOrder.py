# Level Order Traversal using general Method

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def height(root):
    if not root:
        return 0
    
    if root:
        lheight = height(root.left)
        rheight = height(root.right)
        
    return max(lheight, rheight)+1
    
    
def printLevel(root, level):
    if not root:
        return 0
        
    if level==1:
        print(root.data," ")
    
    elif level>1:
        printLevel(root.left, level-1)
        printLevel(root.right, level-1)
        
        
def levelOrder(root):
    ht = height(root)
    
    for i in range(1,ht+1):
        printLevel(root, i)
        

root = Tree(90)
root.left = Tree(80)
root.right = Tree(75)
root.left.left = Tree(70)
root.left.right =Tree(79)
root.right.left = Tree(69)
root.right.right = Tree(65)


print("Height of a tree: ", height(root))
print("Level Order Traversal: ")
levelOrder(root)
