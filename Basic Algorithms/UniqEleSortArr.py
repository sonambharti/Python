#find unique element from a paired sorted array
def solve(n, nums):
    # CODE HERE

    if(n == 1):
        return nums[0]

    return solve(n//2,nums[:n//2]) ^ solve(n-n//2,nums[n//2:])
        


if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	res = solve(n, nums)
	print(res)
