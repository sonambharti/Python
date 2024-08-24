# Zig Zag Level Order Traversal using Dequeue

from collections import deque

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def zigZagLevelOrder(root):
    level = []
    lst = []
    even = True
        
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
            if even:
                lst.append(level)
            else:
                lst.append(level[::-1])
                
            level = []
            
            if Q:
                Q.appendleft(None)
            else:
                break
            even = not even
            
    return lst

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



print("Level Order Traversal Using Dequeue: ")
level = zigZagLevelOrder(root)
print(level)
