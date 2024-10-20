'''
# Nearest multiple of 10

A string str is given to represent a positive number. The task is to round str to the nearest 
multiple of 10.  If you have two multiples equally apart from str, choose the smallest element among them.

Examples:

Input: str = 29 
Output: 30
Explanation: Close multiples are 20 and 30, and 30 is the nearest to 29. 
Input: str = 15
Output: 10
Explanation: 10 and 20 are equally distant multiples from 20. The smallest of the two is 10.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

'''


def roundToNearest(s) : 
    #Complete the function
    n = len(s)
    if(int(s[n-1])<=5):
        s = s[:n-1] + '0'
        return s
    s = s[:n-1] + '0'
   
    i = n-2
    
    while (i>=0 and int(s[i])==9):
        s = s[:i] + '0' + s[i+1:]
        i -= 1
    
    if i < 0:
        s = '1' + s
    else:
        s = s[:i] + str((int(s[i]) + 1)) + s[i+1:]
        
    return s
    
if __name__ == "__main__":
    s = '29'
    res = roundToNearest (s) 
    print(res)
