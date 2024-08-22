"""
# Alien Dictionary

Given a sorted dictionary of an alien language having N words and k starting alphabets of 
standard dictionary. Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid 
order and output will be 1 if the order of string returned by the function is correct else 
0 denoting incorrect string returned.
 

Examples :

Input:  N = 5, K = 4, dict = {"baa","abcd","abca","cab","cad"}
Output: 1
Explanation: Here order of characters is 'b', 'd', 'a', 'c' Note that words are sorted and 
in the given language "baa" comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.


Input: N = 3, K = 3, dict = {"caa","aaa","aab"}
Output: 1
Explanation: Here order of characters is 'c', 'a', 'b' Note that words are sorted and in the 
given language "caa" comes before "aaa", therefore 'c' is before 'a' in output.
Similarly we can find other orders.

 
"""

from collections import deque
adjList = []
    
def topoSort(V, adj):
    # Code here
    in_degree = {i: 0 for i in range(V)}
    res = []
    for i in range(V):
        for node in adj[i]:
            in_degree[node] += 1
    # print("indegree: ", in_degree)
    
    q = deque()
    for i in in_degree:
        if in_degree[i] == 0:
            q.appendleft(i)
            
    while q:
        el = q.pop()
        # print(el)
        res.append(el)
        for adjel in adj[el]:
            in_degree[adjel] -= 1
            if in_degree[adjel] == 0:
                q.appendleft(adjel)
                # print("Queue: ", q)
    return res

def AlienDictionaryOrder(n, k, alien_dict):
    global adjList
    adjList = [[] for _ in range(k)]
    for i in range(N-1):
        s1 = alien_dict[i]
        s2 = alien_dict[i+1]
        leng = min(len(s1), len(s2))
        
        for ptr in range(leng):
            if s1[ptr] != s2[ptr]:
                # adjList[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                adjList[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                break
    
    sort_lst = topoSort(K, adjList)
    res = ""
    for el in sort_lst:
        temp = chr(el + ord('a'))
        res += " " + temp
    return res
        
    
    
if __name__ == "__main__":
    N = 5 
    K = 4
    dicti = ["baa","abcd","abca","cab","cad"]
    print("Topological Order of the Alien Dictionary: ", AlienDictionaryOrder(N, K, dicti))
