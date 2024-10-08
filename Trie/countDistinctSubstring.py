'''
# Count of distinct substrings

Given a string of length N of lowercase alphabet characters. The task is to complete the 
function countDistinctSubstring(), which returns the count of total number of distinct 
substrings of this string.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T 
test cases follow. Each test case contains a string str.

Output:
For each test case in a new line, output will be an integer denoting count of total number 
of distinct substrings of this string.

User Task:
Since this is a functional problem you don't have to worry about input, you just have to 
complete the function countDistinctSubstring().

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 1000

Example(To be used only for expected output):
Input:
2
ab
ababa

Output:
4
10

Exaplanation:
Testcase 1: For the given string "ab" the total distinct substrings are: "", "a", "b", "ab"
'''

class Trie:
    def __init__(self): 
        self.children = [None]*26

count = 1

def Trie_countDistinctSubstring(word):
    # insert function of Trie data structure
    root = Trie()
    global count 
    n = len(word)
    for i in range(n):
        node = root
        for j in range(i, n):
            ch = word[j]
            ind=ord(ch)-ord("a")
            if node.children[ind] is None:
                node.children[ind]=Trie()
                count += 1
            node=node.children[ind]
    

def brute_countDistinctSubstring(s):
    #code here
    st = set()
    n = len(s)
    
    for i in range(n):
        str = ""
        for j in range(i, n):
            str += s[j]
            st.add(str)
    return len(st)+1 # adding 1 for empty string
    
 
if __name__ == "__main__":
    s = "abab"
    res = brute_countDistinctSubstring(s)
    print("Count of Distinct Substring is: ", res)
    
    Trie_countDistinctSubstring(s)
    
    print("No. of distinct substring = ", count)
    
    
    
