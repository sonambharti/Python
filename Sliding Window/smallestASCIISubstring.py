'''
# Smallest Substring

Geek has a string "str" of lowercase letters and an integer k. He wants to 
find out the substring of length k, with the lowest score. The score of a 
string is the sum of the ASCII value of each character present in the string.
Help him to find out the substring. If multiple substrings have the same score,
select the one with the smallest starting index.

Example 1:
    Input:
        str = "hello"
        k = 2
    Output:
        he
    
Example 2:
    Input:
        str = "geeksforgeeks"
        k = 5
    Output:
        eeksf

'''

def smallestSubstring(s, k):
        # code here
    # Sliding Window approach
    n = len(s)
    summ, min_idx = 0, 0
    res = ""
    for i in range(k):
        summ += ord(s[i])
    minm = summ
    for i in range(k, n):
        prev = ord(s[i-k])
        summ -= prev
        summ += ord(s[i])
        if summ < minm:
            minm = summ
            min_idx = i-k+1;
    res = s[min_idx:min_idx+k]
    return res


if __name__ == "__main__":
    # s = 'hello'
    # k = 2
    s = 'geeksforgeeks' # output: eeksf
    k = 5
    res = smallestSubstring(s, k)
    print(res)
