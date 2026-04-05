# Find Longest Zig Zag Path in a tree

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def zigZagLevelPath(root, isLeft, k):
    if root:
        if isLeft:
            return max(zigZagLevelPath(root.left, True, 1), zigZagLevelPath(root.right, False, k+1))
        
        else:
            return max(zigZagLevelPath(root.left, True, k+1), zigZagLevelPath(root.right, False, 1))
    
    return k-1
    
    
    
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


level = zigZagLevelPath(root, True, 0)
print("Longest Zigzag Path:  ", level)
