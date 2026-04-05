#Print path from one given node to other given node

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
        
    
def printPath(root, x1, x2):
    lst1 = []
    lst2 = []
    
    hasPath(root, lst1, x1)
    hasPath(root, lst2, x2)
    
    i, j = 0, 0
    intersection = -1
    
    while(i != len(lst1) or j != len(lst2)):
        #keep moving forward till intersection found
        
        if (i==j and lst1[i] == lst2[j]):
            i += 1
            j += 1
            
        else:
            intersection = j-1
            break
        
    for i in range(len(lst1)-1, intersection-1, -1):
        print(lst1[i], end=" -- ")
        
    for j in range(intersection+1,len(lst1)-1):
        print(lst2[j], end=" -- ")
    print(lst2[-1])
            

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

x1 = int(input("Enter the 1st node to find: "))
x2 = int(input("Enter the 2nd node to find: "))

print("The path from {} to {} is:".format(x1, x2))
printPath(root, x1, x2)

