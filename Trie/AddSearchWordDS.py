"""
# 211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""

from collections import defaultdict

class WordDictionary:

    def __init__(self, endOfWord: bool = False):
        self.children: dict = defaultdict(WordDictionary)
        self.endOfWord: bool = endOfWord

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.children[ch]
        node.endOfWord = True
        

    def search(self, word: str) -> bool:
        node = self
        for idx, char in enumerate(word):
            if char == '.':
                for ch in node.children.values():
                    if ch.search(word[idx+1:]):
                        return True
            if char not in node.children:
                return False
            
            node = node.children[char]
        return node.endOfWord
        
        
if __name__ == "__main__":
    commands = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    words = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    
    obj = None
    output = []

    for cmd, arg in zip(commands, words):
        if cmd == "WordDictionary":
            obj = WordDictionary()
            output.append('null')
        elif cmd == "addWord":
            obj.addWord(arg[0])
            output.append('null')
        elif cmd == "search":
            res = obj.search(arg[0])
            output.append(res)
    
    print(output)
