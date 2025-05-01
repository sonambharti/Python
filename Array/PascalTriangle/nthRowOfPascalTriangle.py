'''
#   Pascal Triangle

Given a positive integer n, return the nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by 
summing up the elements of previous row.


Examples:

Input: n = 4
Output: [1, 3, 3, 1]
Explanation: 4th row of pascal's triangle is [1, 3, 3, 1].

Input: n = 5
Output: [1, 4, 6, 4, 1]
Explanation: 5th row of pascal's triangle is [1, 4, 6, 4, 1].

Input: n = 1
Output: [1]
Explanation: 1st row of pascal's triangle is [1].
'''


def nthRowOfPascalTriangle(n):
    # code here
    res = [1]*n
    ans = 1
    
    for i in range(1, n):
        ans *= n-i
        ans //= i
        res[i] = ans
    return res
    
if __name__ == "__main__":
    n = 5
    print("nth row of Pascal Triangle: ", nthRowOfPascalTriangle(n))
