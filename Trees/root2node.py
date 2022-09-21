#Print path from root to a given node

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def hasPath(root, lst, x):
    #find path from root to x
        
    if not root:
        return False
        
    #push the node in array
    lst.append(root.data)
        
    if root.data == x:
        return True
            
    if(hasPath(root.left, lst, x) or hasPath(root.right, lst, x)):
        return True
            
    #if requested node value is niether in left subtree nor in right subtree, then pop the current node and return False
            
    lst.pop()
    return False
        
    
def printPath(root, x):
    lst = []
        
    if(hasPath(root, lst, x)):
        for i in range(len(lst)-1):
            print(lst[i], end = " -- ")
        print(lst[-1])
            
    else:
        print("No Path found")
            
            

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

#Enter the node value to find and call the function

x = int(input("Enter the node to find: "))
printPath(root, x)

