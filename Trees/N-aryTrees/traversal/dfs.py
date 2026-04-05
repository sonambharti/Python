'''
Create dynamic N-ary tree.

Example:

        A
     /  |  \
    B   C   D
   / \   \
  E   F   G
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def remove_child(self, child_node):
        if child_node in self.children:
            self.children.remove(child_node)
            child_node.parent = None
            

class NAryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def find(self, node, value):
        if node.value == value:
            return node

        for child in node.children:
            found = self.find(child, value)
            if found:
                return found

        return None

    def add_node(self, parent_value, value):
        parent = self.find(self.root, parent_value)

        if not parent:
            raise Exception("Parent not found")

        new_node = TreeNode(value)
        parent.add_child(new_node)

    def remove_node(self, value):
        node = self.find(self.root, value)

        if not node or node == self.root:
            return

        parent = node.parent
        parent.remove_child(node)
        

def dfs(node):
    print(node.value)
    
    for child in node.children:
        dfs(child)
        
        
if __name__ == "__main__":
    tree = NAryTree("A")
    
    tree.add_node("A", "B")
    tree.add_node("A", "C")
    tree.add_node("A", "D")
    
    tree.add_node("B", "E")
    tree.add_node("B", "F")
    
    tree.add_node("C", "G")
    
    print("DFS")
    dfs(tree.root)
    
    print("BFS")
    bfs(tree.root)
