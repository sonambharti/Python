#Find unique element from a list
def solve(n, nums):
    # CODE HERE
    res = nums[0]
    for i in range(1,n):
        res = res ^ nums[i]

    return res

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	res = solve(n, nums)
	print(res)
