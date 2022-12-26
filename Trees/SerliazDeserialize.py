"""
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.
"""

class Node:
    def __init__(self, node):
        self.val = node
        self.left = None
        self.right = None
        
        
class Codec:
    
    def serialize(self, root):
        """
        Encodes a tree to a single string.
       
        :type root: TreeNode
        :rtype: str
        """
        if root:
            return str(root.val) + "(" + self.serialize(root.left) + ")(" + self.serialize(root.right) + ")"
        return "X"

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="X":
            return None
        
        data = data.split("(", 1)
        root = Node(int(data[0]))
        count = 1
        data = data[1]
        
        for i in range(len(data)):
            if data[i]=="(":
                count += 1
            elif data[i]==")":
                count-=1
                if count==0:
                    root.left = self.deserialize(data[:i])
                    root.right = self.deserialize(data[i+2:-1])
                    return root
                    
                
def inorder(root, lst):
    # CODE HERE
    if not root:
        return
    inorder(root.left, lst)
    lst.append(root.val)
    inorder(root.right, lst)

   
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

lst = []
obj = Codec()
res1 = obj.serialize(root)
print(res1)
res2 = obj.deserialize(res1)
print(res2)
inorder(res2, lst)
print("Inorder Traversal: ", lst)
