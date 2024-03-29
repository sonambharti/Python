#Quesion asked in Amazon Interviews
"""
Find the length of largest possible palindromic string from a given string.

Input:
str = "abccccdd"

Output:
7

Input: 
str = "abccedacdbct"

Output: 11

"""

def longestPalindrome(s):
    s = set(str)
    # print(s)
    res = []
    
    for i in s:
        res.append(str.count(i))
        
    # print(res)
    countLength = 0
    for i in range(len(res)):
        if res[i]%2 != 0:
           countLength += res[i]-1
           res[i] = res[i]%2
        else:
            countLength += res[i]
       
    if 1 in res:
        return countLength+1
    return countLength


if __name__ == "__main__":
    # str = "abccedacdbct"
    str = "abccdacdbccd"
    # str = "abccccdd"
    ans = longestPalindrome(str)
    print("Length of the largest possible palindromic string: ", ans)
