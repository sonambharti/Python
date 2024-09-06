'''
# Nth Natural Number

Given a positive integer n. You have to find nth natural number after removing all 
the numbers containing the digit 9.

Examples :

Input: n = 8
Output: 8
Explanation: After removing natural numbers which contains digit 9, first 8 numbers 
are 1,2,3,4,5,6,7,8 and 8th number is 8.
Input: n = 9
Output: 10
Explanation: After removing natural numbers which contains digit 9, first 9 numbers 
are 1,2,3,4,5,6,7,8,10 and 9th number is 10.

Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)

'''

def findNth(n):
    #code here
    res, multiplier = 0, 1
    
    while n > 0:
        # find last base-9 digit
        digit = n % 9
        
        # convert it to decimal and add it to res
        res += digit * multiplier
        
        # multiply 10 to place a digit
        multiplier *= 10
        
        # update n by dividing it by 9
        n //= 9
    
    return res

    
if __name__ == "__main__":
    n = 4
    res = findNth(n)
    print("The nth natural number after removing all the numbers containing the digit 9: ", res)

	
