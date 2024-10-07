"""
# Longest Common Prefix

Given an array of strings arr. Return the longest common prefix among each and every 
strings present in the array. If there's no prefix common in all the strings, return "-1".

Examples :

Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
Output: gee
Explanation: "gee" is the longest common prefix in all the given strings.
Input: arr[] = ["hello", "world"]
Output: -1
Explanation: There's no common prefix in the given strings.
Expected Time Complexity: O(n*min(|arri|))
Expected Space Complexity: O(min(|arri|))

"""

def longestCommonPrefix(arr):
    # code here
    n = len(arr)
    Flag = True
    alen = []
    for i in range(len(arr)):
        alen.append(len(arr[i]))
    minm = min(alen) # minm=len(min(arr,key=len))
    res=""
    for i in range(minm):
        for word in arr:
            if arr[0][i] != word[i]:
                Flag = False
                break
        if Flag:
            res += arr[0][i]
    return "-1" if len(res) == 0 else res


    
    
if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    res = longestCommonPrefix(arr)
    print("The Longest Common Prefix is: ", res)
