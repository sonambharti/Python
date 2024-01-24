"""
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""

def validPalindrome(s):
    
    str = ""
    
    for i in s:
        if i.isalpha() == True:
            str += i
    
    str = str.lower()
    start = 0
    end = len(str) - 1
    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    
    return True


if __name__ == "__main__":
    # s = "Malayalam"
    s = "A man, a plan, a canal: Panama"
    res = validPalindrome(s)
    print("Is a valid palindrome: ", res)
        
    
