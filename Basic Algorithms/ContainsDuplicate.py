def solve(n, arr):
  # CODE HERE
  set1 = set(arr)
  lst = list(set1)

  if(len(lst) == n):
    return 0
  else:
    return 1

if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	res = solve(n, arr)
	print(res)
