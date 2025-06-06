'''
# Count Subarrays

Given an array , count the number of subarrays of array A which are non-decreasing.
A subarray A[i,j], where 1≤i≤j≤N is a sequence of integers Ai, ..., Aj.
You have to count the total number of such subarrays.

Input
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains a single integer N denoting the size of array.

The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output
For each test case, output in a single line the required answer.


Input:
2
4
1 4 2 3
1
5

Output:
6
1

'''


# cook your dish here
def countSubArr(n, arr):
    dp = [1]*n 
    ans = 1
    for i in range(1, n):
        if arr[i-1] <= arr[i]:
            dp[i] += dp[i-1] 
        ans += dp[i]
    return ans


if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int,input().split()))
        res = countSubArr(n, arr)
        print(res)
        t -= 1
