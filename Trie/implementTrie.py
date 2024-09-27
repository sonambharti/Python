'''
# 208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
store and retrieve keys in a dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was 
inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string 
word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


'''

class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['*']=''

        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return '*' in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
        
        
if __name__ == "__main__":
    obj = Trie()
    # obj.insert(word)
    obj.insert("apple")
    obj.insert("apron")
    obj.insert("apps")
    obj.insert("bat")
    obj.insert("ball")
    obj.insert("cinderalla")
    
    param_2 = obj.search("cinderalla")
    print("If cinderalla is there in DS or not: ", param_2)
    
    param_3 = obj.startsWith("cind")
    print("If there exists a word start with `cind` or not: ", param_3)
    
    
    
