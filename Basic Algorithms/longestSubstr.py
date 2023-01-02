#Length of longest substring without repeatation....
def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0

    maxmlen = 0
    substr = set()
    l = 0
    for r in range(len(s)):
        while s[r] in substr:
            substr.remove(s[l])
            l+=1
        substr.add(s[r])
        maxmlen = max(maxmlen, r-l+1)
        
    #print(substr)
    return maxmlen
    
if __name__ == "__main__":
    str = input("Enter a string: ")
    maxmlength = lengthOfLongestSubstring(str)
    print("The length of the longest substring in the given string: ",maxmlength)
