'''
# Longest Prefix Suffix

Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.

NOTE: Prefix and suffix can be overlapping but they should not be equal to the entire string.

Examples :

Input: str = "abab"
Output: 2
Explanation: "ab" is the longest proper prefix and suffix. 
Input: str = "aaaa"
Output: 3
Explanation: "aaa" is the longest proper prefix and suffix. 
Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(|str|)

'''


def lps(s):
	# code here
    n = len(s)
    lps = [0] * n  # lps array to store the length of the longest prefix suffix
    length = 0  # length of the previous longest prefix suffix
    
    i = 1  # start from the second character of the string
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # try for the previous position
            else:
                lps[i] = 0
                i += 1

    return lps[-1]  # return the last value in the lps array


if __name__ == "__main__":
    s = "abab"
    res = lps(s)
    print("Longest Prefix Suffix: ", res)
    
