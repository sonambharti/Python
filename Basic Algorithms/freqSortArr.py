def solve(n, nums, k):
    # CODE HERE
    count = 0
    for i in range(n):
        if(nums[i] == k):
            count += 1
    
    return count

if __name__ == '__main__':
	n = int(input())
	nums = []
	print("Enter array element: ")
	#nums = list(map(int, input().split()))
	for i in range(n):
	    ele = int(input())
	    nums.append(ele)
	k = int(input())
	res = solve(n, nums, k)
	print(res)
