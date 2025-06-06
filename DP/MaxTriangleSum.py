'''
# Sums in a Triangle

Given an integer N, let us consider a triangle of numbers of N lines in which a number a11
appears in the first line, two numbers a21 and a22 appear in the second line, three numbers a31, a32 and a33​ 
appear in the third line, etc. In general, i numbers​ appear in the ith line for all 1≤i≤N. Develop a program that will compute
the largest of the sums of numbers that appear on the paths starting from the top towards the base, so that:

on each path the next number is located on the row below, more precisely either directly below or below and one place to the right.
Warning: large Input/Output data, be careful with certain languages

Input Format
The first line of the input contains an integer T, the number of test cases.
Then T test cases follow. Each test case starts with an integer N, the number of rows. Then N lines follow where in ith
line contains i integers.

Output Format
For each test case print the maximum path sum in a separate line.

Input 1:
3
1
2 1
1 2 3

Output 1:
5


Input 2:
4
1
1 2
4 1 2
2 3 1 1

Output 2:
9
'''


# cook your dish here
def MaxTriangleSum(arr):
    dp = [[0]*(n + 1) for _ in range(n + 1)]
    
    # Fill the last row of dp with values from arr
    for j in range(n):
        dp[n - 1][j + 1] = arr[n - 1][j]
    
    # Fill the dp array from bottom to top 
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j+1] = arr[i][j] + max(dp[i+1][j+1], dp[i+1][j+2])
    
    return dp[0][1]
        
    

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        row = list(map(int,input().split()))
        arr.append(row)
    res = MaxTriangleSum(arr)
    print(res)
    
