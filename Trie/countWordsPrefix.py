"""
Implement Trie to count no. of words or prefixes present in the Trie data structure. Also,
Implement the delete or erase function for the Trie data structure.
"""                            
class Node:
    def __init__(self):
        # Array to store links to child nodes
        self.links = [None] * 26
        # Counter for number of words that end at this node
        self.cntEndWith = 0
        # Counter for number of words that have this node as a prefix
        self.cntPrefix = 0
        
    # Check if the node contains a specific key (letter)
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    # Insert a new node with a specific key (letter) into the Trie
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    # Get the node with a specific key (letter) from the Trie
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def increase_end(self):
        """
        Function to increment the count
        of words that end at this node.
        """
        # Increment the counter
        self.cntEndWith += 1

    def increase_prefix(self):
        """
        Function to increment the count of
        words that have this node as a prefix.
        """
        # Increment the counter
        self.cntPrefix += 1
    
    def delete_end(self):
        """
        Function to decrement the count of
        words that end at this node.
        """
        # Decrement the counter
        self.cntEndWith -= 1

    def reduce_prefix(self):
        """
        Function to decrement the count of 
        words that have this node as a prefix.
        """
        # Decrement the counter
        self.cntPrefix -= 1


class Trie:
    def __init__(self):
        # Constructor to initialize the
        # Trie with an empty root node
        self.root = Node()

    # Inserts a word into the Trie
    # Time Complexity O(len), where len is the length of the word
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                # Create a new node for the letter if not present
                node.put(ch, Node())
            # Move to the next node
            node = node.get(ch)
            # Increase the count of the prefix
            node.increase_prefix()
        # Mark the end of the word
        node.increase_end()

    
    def count_words_equal_to(self, word):
        """
        Function to count the number
        of words equal to a given word.
        """
        # Start from the root node
        node = self.root
        # Iterate over each character in the word
        for ch in word:
            # If the character is found in the trie
            if node.containsKey(ch):
                # Move to the child node corresponding to the character
                node = node.get(ch)
            else:
                # Return 0 if the character is not found
                return 0
        # Return the count of  words ending at the node
        return node.cntEndWith
        
    def count_words_starting_with(self, word):
        """
        Function to count the number of
        words starting with a given prefix.
        """
        # Start from the root node
        node = self.root
        # Iterate over each
        # character in the prefix
        for ch in word:
            # If the character is
            # found in the trie
            if node.containsKey(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
            else:
                # Return 0 if the
                # character is not found
                return 0
        # Return the count of
        # words with the prefix
        return node.cntPrefix
        
        
    def erase(self, word):
        """
        Function to erase
        a word from the trie.
        """
        # Start from the root node
        node = self.root
        # Iterate over each
        # character in the word
        for ch in word:
            # If the character is
            # found in the trie
            if node.containsKey(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
                # Decrement the prefix
                # count for the node
                node.reduce_prefix()
            else:
                # Return if the
                # character is not found
                return
        # Decrement the end count
        # for the last node of the word
        node.delete_end()


if __name__ == "__main__":
    trie = Trie()
    print("Inserting words: Striver, Striving, String, Strike")
    trie.insert("apple")
    trie.insert("appron")
    trie.insert("apps")
    trie.insert("apple")
    trie.insert("cinderalla")

    print("Inserting strings 'apple', 'app' into Trie")
    print("Count Words Equal to 'apple':", trie.count_words_equal_to("apple"))
    print("Count Words Starting With 'app':", trie.count_words_starting_with("app"))
    print("Erasing word 'app' from trie")
    trie.erase("app")
    print("Count Words Equal to 'apple':", trie.count_words_equal_to("apple"))
    print("Count Words Starting With 'apple':", trie.count_words_starting_with("app"))
                           
                        
