'''
#   191. Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
'''
class TrieNode:
    def __init__(self):
        # Initialize a TrieNode with an empty dictionary for children nodes,
        # a boolean flag to indicate if it represents the end of a word,
        # and a reference counter.
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        # Method to add a word to the trie.
        # Traverse the trie, creating nodes as necessary.
        # Increment the reference counter for each visited node.
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        # Method to remove a word from the trie.
        # Decrement the reference counter for each visited node.
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie implementation to efficiently search words on the board.
        root = TrieNode()
        # Add all words from the dictionary to the trie.
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        result, visit = set(), set()

        def dfs(r, c, node, word):
            # Depth-first search to explore possible word paths on the board.
            # Check boundary conditions, character existence, and node references.
            if (
                r not in range(rows) 
                or c not in range(cols)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                # If a word is found, add it to the result set,
                # mark it as not a word in the trie, and remove it.
                node.isWord = False
                result.add(word)
                root.removeWord(word)

            # Explore all four directions recursively.
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        # Iterate through each cell on the board to start DFS.
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)
    
    
if __name__ == "__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] 
    words = ["oath","pea","eat","rain"]
    obj = Solution()
    res = obj.findWords(board, words)
    print("Words present in the board: ", res)
