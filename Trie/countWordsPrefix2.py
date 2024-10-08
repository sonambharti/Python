'''
Implement Trie to count no. of words or prefixes present in the Trie data structure.
'''

class Node:
    def __init__(self): 
        self.children = [None]*26
  
        self.cntEndWith = 0
        # Counter for number of words that have this node as a prefix
        self.cntPrefix = 0


class Trie:
    def __init__(self):
        # Constructor to initialize the Trie with an empty root node
        self.root = Node()

    
def insert(root, word):
    for ch in word:
        ind=ord(ch)-ord("a")
        if root.children[ind] is None:
            root.children[ind]=Node()
        root=root.children[ind]
        root.cntPrefix += 1
    root.cntEndWith+=1

def count_words_equal_to(root, word):
    # Iterate over each character in the word
    for ch in word:
        ind=ord(ch)-ord("a")
        # If the character is found in the trie
        if root.children[ind] is not None:
            # Move to the child node corresponding to the character
            root=root.children[ind]
        else:
            # Return 0 if the character is not found
            return 0
    # Return the count of  words ending at the node
    return root.cntEndWith
    
def count_prefix(root, word):
    # Iterate over each character in the word
    for ch in word:
        ind=ord(ch)-ord("a")
        # If the character is found in the trie
        if root.children[ind] is not None:
            # Move to the child node corresponding to the character
            root=root.children[ind]
        else:
            # Return 0 if the character is not found
            return 0
    # Return the count of  words prefix
    return root.cntPrefix
    
 
if __name__ == "__main__":
    trie = Trie()
    # obj.insert(word)
    insert(trie.root,"apple")
    insert(trie.root,"apple")
    insert(trie.root,"apps")
    insert(trie.root,"bat")
    insert(trie.root,"ball")
    insert(trie.root,"cinderalla")
    
    param_2 = count_words_equal_to(trie.root,"apple")
    print("If apple is there in DS or not: ", param_2)
    
    param_3 = count_prefix(trie.root,"app")
    print("If there exists a word start with `app` or not: ", param_3)
    
    
    
