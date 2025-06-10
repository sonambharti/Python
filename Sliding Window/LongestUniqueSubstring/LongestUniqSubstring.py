"""
# Find the length  of the longest substring having unique characters.

Example:
Input:
s = "pwewe"
Output: 3
"""
# Brute Force O(n^3)
def LongestUniqSubstring_brute(s):
    n = len(s)
    max_len = 0
    seen = set()
    res = ""
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
        # max_len = max(max_len, len(seen))
        if len(seen) > max_len :
            max_len = len(seen)
            res = s[i:i+len(seen)]
    return max_len, res
    

# Optimized approach O(n)
def LongestUniqSubstring(s):
    last_seen = {}
    left, start = 0, 0
    max_len = 0
    res = ""
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1 
        last_seen[char] = right
        window_len = right - left + 1
        if window_len > max_len:
            max_len = window_len
            start = left
        res = s[start : start+max_len]
    return max_len, res
    
if __name__ == "__main__":
    s = "umnlnlecabi"
    # s = 'pweweqt'
    print("Brute Force: ", LongestUniqSubstring_brute(s))
    print(LongestUniqSubstring(s))
    
