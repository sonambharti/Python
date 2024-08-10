'''
# Array building from permutation

From a zero-based permutation nums (0-indexed), we have to build an array(ans) of same length where 
ans[i] = nums[nums[i]] for each 0 <= i < nums.length and then return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

Example:

Input: n = 6, arr = [0, 2, 1, 5, 3, 4]
Output: [0, 1, 2, 4, 5, 3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
= [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
= [0,1,2,4,5,3]

'''

def buildArrPermute(n, arr):
    # CODE HERE

    ans = [1]*n

    for i in range(n):
        ans[i] = arr[arr[i]]

    return ans

if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	out = buildArrPermute(n, arr)
	print(*out)
