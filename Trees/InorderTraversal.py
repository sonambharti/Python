class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder(root):
    if root:
            
        inorder(root.left)
        print(root.data)
        inorder(root.right)



root = Tree(90)
root.left = Tree(80)
root.right = Tree(75)
root.left.left = Tree(70)
root.left.right =Tree(79)
root.right.left = Tree(69)
root.right.right = Tree(65)

print("Inorder Traversal")
inorder(root)
