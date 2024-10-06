                            
class Node:
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False

    

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
    root.isEndOfWord=True


# Returns if the word is in the trie
def search(root, word):
    for ch in word:
        ind=ord(ch)-ord("a")
        if root.children[ind] is None:
            # If a letter is not found, the word is not in the Trie
            return False
        # Move to the next node
        root=root.children[ind]
    # Check if the last node marks the end of a word
    return root.isEndOfWord


# Returns if there is any word in the trie that starts with the given prefix
def startsWith(root, prefix):
    for ch in prefix:
        ind=ord(ch)-ord("a")
        if root.children[ind] is None:
            # If a letter is not found, there is no word with the given prefix
            return False
        # Move to the next node
        root=root.children[ind]
    # The prefix is found in the Trie
    return True


if __name__ == "__main__":
    trie = Trie()
    print("Inserting words: apple, apron, apps, bat, ball")
    insert(trie.root, "apple")
    insert(trie.root, "apron")
    insert(trie.root, "apps")

    print("Search if apple exists in trie: " +
          ("True" if search(trie.root, "apple") else "False"))
          
    insert(trie.root, "bat")
    insert(trie.root, "ball")

    print("Search if Strawberry exists in trie: " +
          ("True" if search(trie.root, "strawberry") else "False"))

    print("Search if cinderalla exists in trie: " +
          ("True" if search(trie.root, "cinderalla") else "False"))

    print("Search if ball exists in trie: " +
          ("True" if search(trie.root, "ball") else "False"))

    print("If words in Trie start with cind: " +
          ("True" if startsWith(trie.root, "bal") else "False"))
                           
                        
