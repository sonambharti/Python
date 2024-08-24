class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def preorder(root):
    if root:
        print(root.data)    
        preorder(root.left)
        preorder(root.right)
        
        

root = Tree(90)
root.left = Tree(80)
root.right = Tree(75)
root.left.left = Tree(70)
root.left.right =Tree(79)
root.right.left = Tree(69)
root.right.right = Tree(65)

print("preorder Traversal")
preorder(root)
