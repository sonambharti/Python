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
        
        
        

root = Tree(90)
root.left = Tree(80)
root.right = Tree(75)
root.left.left = Tree(70)
root.left.right =Tree(79)
root.right.left = Tree(69)
root.right.right = Tree(65)


print("Height of a tree")
print(height(root))

