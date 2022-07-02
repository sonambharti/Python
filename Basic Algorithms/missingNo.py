#find missing no between a given range
def solve(n, arr):
    # CODE HERE
    res = []
    for i in range(0,n+2):
        if i not in arr:
            res.append(i)

    return res

  
if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	res = solve(n, arr)
	print(*res)
